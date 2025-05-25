#!/usr/bin/env python3
"""
monitor.py — Keep-alive heartbeat & stall detector

Run standalone:
    python monitor.py --cmd "python heavy_job.py" --interval 30

Or import:
    from monitor import start_heartbeat
    start_heartbeat(interval=30, cpu_thresh=1.0, samples=4)
"""

import argparse, logging, os, shlex, subprocess, sys, threading, time
from datetime import datetime
from typing import Optional

import psutil

# ---------------- CONFIG -----------------
LOG_FMT = "%(asctime)s [HEARTBEAT] %(message)s"
logging.basicConfig(
    stream=sys.stdout, level=logging.INFO, format=LOG_FMT, datefmt="%Y-%m-%d %H:%M:%S"
)
# -----------------------------------------


def _sampler(pid: int, interval: int, cpu_thresh: float, samples: int, on_stall):
    """
    Sample CPU & IO; call `on_stall()` if below threshold for `samples`
    consecutive intervals.
    """
    proc = psutil.Process(pid)
    low_count = 0
    while proc.is_running():
        try:
            cpu = proc.cpu_percent(interval=None)  # instant pct since last call
            io = proc.io_counters().read_bytes + proc.io_counters().write_bytes
            time.sleep(interval)
            cpu_now = proc.cpu_percent(interval=None) / psutil.cpu_count()
            io_now = proc.io_counters().read_bytes + proc.io_counters().write_bytes
            cpu_delta = cpu_now
            io_delta = io_now - io
            if cpu_delta < cpu_thresh and io_delta == 0:
                low_count += 1
                if low_count >= samples:
                    on_stall(cpu_delta, io_delta)
                    low_count = 0  # reset so we warn again after next window
            else:
                low_count = 0  # activity resumed
        except psutil.NoSuchProcess:
            break


def _heartbeat(interval: int):
    while True:
        logging.info("still running…")
        time.sleep(interval)


def start_heartbeat(
    interval: int = 60,
    cpu_thresh: float = 1.0,
    samples: int = 3,
    pid: Optional[int] = None,
):
    """
    Fire-and-forget: starts background threads that
    1) log a heartbeat every `interval` seconds
    2) warn if CPU & IO stay idle for `samples` * `interval` seconds

    Parameters
    ----------
    interval : int
        Seconds between heartbeats / samples.
    cpu_thresh : float
        CPU % below which activity is considered idle.
    samples : int
        Number of consecutive idle samples before flagging a stall.
    pid : int, optional
        Process ID to monitor; defaults to current PID.
    """
    pid = pid or os.getpid()

    def warn(cpu, io):
        logging.warning(f"⚠️  Possible stall: cpu={cpu:.2f}% Δio={io} bytes")

    threading.Thread(target=_heartbeat, args=(interval,), daemon=True).start()

    threading.Thread(
        target=_sampler, args=(pid, interval, cpu_thresh, samples, warn), daemon=True
    ).start()


# ---------- CLI wrapper mode -------------


def main():
    parser = argparse.ArgumentParser(description="Heartbeat & stall monitor")
    parser.add_argument("--cmd", help="Command to run & monitor")
    parser.add_argument(
        "--interval", type=int, default=60, help="Seconds between heartbeats"
    )
    parser.add_argument(
        "--cpu-thresh",
        type=float,
        default=1.0,
        help="CPU %% below which activity is idle",
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=3,
        help="Consecutive idle samples for stall alert",
    )
    args = parser.parse_args()

    if not args.cmd:
        parser.error("--cmd required when running standalone")

    logging.info(f"Launching: {args.cmd}")
    proc = subprocess.Popen(shlex.split(args.cmd))
    start_heartbeat(
        interval=args.interval,
        cpu_thresh=args.cpu_thresh,
        samples=args.samples,
        pid=proc.pid,
    )

    proc.wait()
    logging.info(f"Process exited with code {proc.returncode}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
