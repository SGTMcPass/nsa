import os
import re
import curses
from pathlib import Path

def adjust_heading_levels(content: str) -> str:
    return re.sub(r'^(#+)', r'#\1', content, flags=re.MULTILINE)

def collect_md_files(directory: Path) -> list:
    return sorted([
        f for f in directory.rglob("*.md")
        if not any(part.startswith('.') for part in f.parts)
    ])

def build_toc(file_list):
    toc = ["# Table of Contents\n"]
    for f in file_list:
        section = str(f).replace(" ", "-").replace("/", "-").replace("\\", "-").lower()
        toc.append(f"- [{f}](#{section})")
    return "\n".join(toc) + "\n\n"

def concatenate_markdown_files(file_list, input_dir, output_file):
    input_path = Path(input_dir).resolve()
    output_path = Path(output_file).resolve()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        toc = build_toc([f.relative_to(input_path) for f in file_list])
        outfile.write(toc)

        for md_file in file_list:
            rel = md_file.relative_to(input_path)
            anchor = str(rel).replace(" ", "-").replace("/", "-").replace("\\", "-").lower()
            outfile.write(f"# {rel}\n<a name=\"{anchor}\"></a>\n\n")

            with open(md_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                adjusted = adjust_heading_levels(content)
                outfile.write(adjusted)
                outfile.write("\n\n---\n\n")

    print(f"\n✅ Combined Markdown written to: {output_path}")

# ---------- UI: Pick Files for Custom Order ----------
def curses_select_and_order(stdscr, files):
    curses.curs_set(0)
    selected = 0
    chosen = []

    while True:
        stdscr.clear()
        stdscr.addstr("Enter to add file → Space to skip → 'f' to finish\n\n", curses.A_BOLD)

        for i, path in enumerate(files):
            marker = "[✔]" if path in chosen else "   "
            style = curses.A_REVERSE if i == selected else curses.A_NORMAL
            stdscr.addstr(f"{marker} {path}\n", style)

        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected = max(0, selected - 1)
        elif key == curses.KEY_DOWN:
            selected = min(len(files) - 1, selected + 1)
        elif key in [10, 13]:  # Enter
            if files[selected] not in chosen:
                chosen.append(files[selected])
        elif key == ord('f'):
            break

    return chosen

# ---------- Entry Point ----------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Concatenate and reorder Markdown files with TOC.")
    parser.add_argument("input_dir", help="Directory containing .md files")
    parser.add_argument("-o", "--output", default="combined.md", help="Output Markdown file name")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    all_files = [f.resolve() for f in collect_md_files(input_dir)]
    if not all_files:
        print("❌ No Markdown files found.")
        exit(1)

    print("🕹️ Launching file selector...")
    selected_files = curses.wrapper(curses_select_and_order, all_files)

    # Include all unselected files in default order
    remaining = [f for f in all_files if f not in selected_files]
    final_file_list = selected_files + remaining

    concatenate_markdown_files(final_file_list, input_dir, args.output)

