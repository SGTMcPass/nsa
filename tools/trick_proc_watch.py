#!/usr/bin/env python3
"""
trick_proc_watch.py — colourful mini-top for S_main* & Python processes
with built-in stall detection, now ignoring its own PID.
"""

import argparse, getpass, os, re, shutil, sys, time
from collections import defaultdict
from typing import List

import psutil

# ── ANSI colours --------------------------------------------------------------
RESET = "\033[0m"; BOLD = "\033[1m"
FG = dict(red="\033[31m", green="\033[32m", yellow="\033[33m",
          magenta="\033[35m", cyan="\033[36m")

def colour(val, mid, high):
    return FG["red"] if val >= high else FG["yellow"] if val >= mid else FG["green"]

# thresholds
CPU_MID,  CPU_HIGH  = 40.0, 80.0   # for colour only
MEM_MID,  MEM_HIGH  = 10.0, 20.0
# stall logic defaults (overridable via CLI)
DEF_CPU_IDLE = 1.0    # %
DEF_SAMPLES  = 3

# ── helpers -------------------------------------------------------------------
def fmt_hms(s: float) -> str: return time.strftime("%H:%M:%S", time.gmtime(s))

def is_target(proc: psutil.Process) -> bool:
    try:
        name = proc.name()
    except psutil.Error:
        return False
    return name.startswith("S_main") or re.fullmatch(r"python(\d+(\.\d+)*)?(\.exe)?", name)

# ── main loop -----------------------------------------------------------------
def watch(user: str, interval: float, cpu_idle: float, samples: int):
    width  = shutil.get_terminal_size(fallback=(120, 20)).columns
    header = (f"{BOLD}{'UID':<8} {'PID':>6} {'PPID':>6} {'CPU%':>5} {'MEM%':>5} "
              f"{'ELAPSED':>8} STATUS CMD{RESET}")
    self_pid = os.getpid()                       # 🔹 our own PID

    state: dict[int, tuple[int, int]] = defaultdict(lambda: (0, 0))
    for p in psutil.process_iter():              # prime cpu%
        try: p.cpu_percent(interval=None)
        except psutil.Error: pass

    while True:
        print("\033[2J\033[H", end="")           # clear + home
        print(header);  print("-" * width)

        for proc in psutil.process_iter(attrs=["pid","ppid","name","username",
                                               "create_time","cmdline"]):
            try:
                if proc.pid == self_pid:                       # 🔹 ignore self
                    continue
                if proc.info["username"] != user or not is_target(proc):
                    continue

                cpu = proc.cpu_percent(interval=None)
                io  = proc.io_counters()
                io_tot = (io.read_bytes + io.write_bytes) if io else 0
                mem = proc.memory_percent()

                prev_io, idle_cnt = state[proc.pid]
                stalled = False
                if cpu < cpu_idle and io_tot == prev_io:
                    idle_cnt += 1
                    if idle_cnt >= samples: stalled = True
                else:
                    idle_cnt = 0
                state[proc.pid] = (io_tot, idle_cnt)

                cpu_s = f"{colour(cpu, CPU_MID, CPU_HIGH)}{cpu:5.1f}{RESET}"
                mem_s = f"{colour(mem, MEM_MID, MEM_HIGH)}{mem:5.1f}{RESET}"
                status = f"{FG['red']}STALL{RESET}" if stalled else "     "

                cmd = " ".join(proc.info['cmdline']) or proc.info['name']
                cmd_col = width - 70 if width > 90 else 20
                name_col = FG["cyan"] if cmd.startswith("S_main") else FG["magenta"]
                cmd_s = f"{name_col}{cmd[:cmd_col]}{RESET}"

                print(f"{user:<8} {proc.pid:>6} {proc.ppid():>6} {cpu_s} {mem_s} "
                      f"{fmt_hms(time.time()-proc.create_time()):>8} {status:>5} {cmd_s}")

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                state.pop(proc.pid, None)
                continue

        sys.stdout.flush()
        time.sleep(interval)

# ── CLI -----------------------------------------------------------------------
def main(argv: List[str] | None = None):
    ap = argparse.ArgumentParser(description="Watch Trick & Python procs with stall flag")
    ap.add_argument("-u","--user", default=getpass.getuser())
    ap.add_argument("-i","--interval", type=float, default=2.0)
    ap.add_argument("--cpu-thresh", type=float, default=DEF_CPU_IDLE,
                    help="below this %%CPU counts as idle")
    ap.add_argument("--samples", type=int, default=DEF_SAMPLES,
                    help="consecutive idle samples ⇢ STALL")
    args = ap.parse_args(argv)
    watch(args.user, args.interval, args.cpu_thresh, args.samples)

if __name__ == "__main__":
    main()

