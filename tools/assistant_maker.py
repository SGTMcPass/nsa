import os
from pathlib import Path


def find_layer_files(base_dir):
    """Recursively find all instructions.md and extension_layers/*.md in profiles."""
    found_files = []
    base = Path(base_dir).resolve()
    for sim_dir in base.glob("**/simulation*"):
        # Find instructions
        instr_dir = sim_dir / "instructions"
        if instr_dir.exists():
            for f in instr_dir.glob("*.md"):
                found_files.append(f)
        # Find extension layers
        ext_dir = sim_dir / "extension_layers"
        if ext_dir.exists():
            for group in ext_dir.iterdir():
                if group.is_dir():
                    for f in group.glob("*.md"):
                        found_files.append(f)
    return found_files


def choose_layers(files):
    """Interactive selection of layers to include."""
    print("\nAvailable files for concatenation:")
    for idx, f in enumerate(files):
        print(f"  [{idx}] {f.relative_to(Path.cwd())}")
    chosen = []
    while True:
        sel = input(
            "\nEnter indices of files to include (comma-separated, in order), or 'd' for default, or 'q' to quit: "
        ).strip()
        if sel.lower() == "d":
            # Default order per your request
            default_names = [
                "instructions/instructions.md",
                "extension_layers/personality/base_sim_assistant_personality.md",
                "extension_layers/planning/sprint.md",
                "extension_layers/heuristics/heuristics.md",
                "extension_layers/modes/modes.md",
                "extension_layers/glossaries/glossary.md",
            ]
            chosen = []
            for name in default_names:
                for f in files:
                    if name in str(f):
                        chosen.append(f)
            break
        elif sel.lower() == "q":
            print("Exiting.")
            exit()
        else:
            try:
                indices = [int(i) for i in sel.split(",") if i.strip().isdigit()]
                chosen = [files[i] for i in indices]
                break
            except Exception as e:
                print(f"Invalid input: {e}")
    return chosen


def make_headers(path):
    """Generate a header from the file path."""
    parts = Path(path).parts
    section = parts[-2] if len(parts) > 1 else ""
    filename = Path(path).stem.replace("_", " ").replace("-", " ").title()
    return f"# {section.upper()} — {filename}\n"


def concatenate_files(file_list, out_path):
    """Concatenate files with section headers."""
    with open(out_path, "w") as fout:
        for f in file_list:
            header = make_headers(f)
            fout.write(header)
            with open(f, "r") as fin:
                fout.write(fin.read())
                fout.write("\n\n")
    print(f"\nConcatenated prompt saved to: {out_path}")


def detect_target_profile(file_list, profiles_dir):
    """
    Detect which direct child of profiles/ contains all selected files.
    If multiple, prompt the user to select.
    """
    candidate_profiles = set()
    for f in file_list:
        rel = f.relative_to(profiles_dir)
        # rel = simulation/extension_layers/personality/base_sim_assistant_personality.md
        # We want the first part
        candidate_profiles.add(rel.parts[0])
    if len(candidate_profiles) == 1:
        profile = candidate_profiles.pop()
    else:
        print("Multiple profile directories detected. Choose one for output:")
        for i, p in enumerate(candidate_profiles):
            print(f"[{i}] {p}")
        sel = int(input("Enter index of output profile: ").strip())
        profile = list(candidate_profiles)[sel]
    return profiles_dir / profile


def main():
    repo_root = Path(__file__).parent.parent.resolve()
    profiles_dir = repo_root / "profiles"
    all_layer_files = find_layer_files(profiles_dir)
    if not all_layer_files:
        print("No assistant prompt files found.")
        return
    to_concat = choose_layers(all_layer_files)
    if not to_concat:
        print("No files selected.")
        return
    # Destination: root of chosen profile (first file's parent .parent.parent)
    target_root = to_concat[0].parents[2]
    target_profile_dir = detect_target_profile(to_concat, profiles_dir)
    out_path = target_profile_dir / "assistant_prompt_combined.md"
    concatenate_files(to_concat, out_path)


if __name__ == "__main__":
    main()
