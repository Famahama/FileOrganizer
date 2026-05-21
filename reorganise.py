"""
reorganise.py  —  Project folder tool for animation & editing teams.

Drop OPEN.bat into any project folder and double-click it.
The GUI opens with the folder pre-filled.
"""

import sys, shutil, threading, json
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# PROJECT TYPE DEFINITIONS
# Each type has a folder structure and a set of file-sorting rules.
# ─────────────────────────────────────────────────────────────────────────────

TYPES = {
    "2d": {
        "label":    "2D Motion Graphics",
        "subtitle": "AE  ·  Illustrator  ·  Photoshop",
        "structure": [
            "00_Project_Files/AfterEffects/projects",
            "00_Project_Files/AfterEffects/ae_cache",
            "00_Project_Files/Illustrator",
            "00_Project_Files/Photoshop",
            "01_Assets/Audio/Music",
            "01_Assets/Audio/SFX",
            "01_Assets/Footage/Raw",
            "01_Assets/Footage/Proxies",
            "01_Assets/Images/References",
            "01_Assets/Fonts",
            "02_Renders/AE_Previews",
            "03_Exports/Drafts/v001",
            "03_Exports/Finals",
            "04_Docs/Brief",
            "04_Docs/References",
            "04_Docs/Feedback",
            "05_Handoff",
        ],
        "rules": [
            {"dest": "00_Project_Files/AfterEffects/projects", "exts": [".aep"],                           "in_folder": "",   "name_has": ""},
            {"dest": "00_Project_Files/Illustrator",           "exts": [".ai"],                            "in_folder": "",   "name_has": ""},
            {"dest": "00_Project_Files/Photoshop",             "exts": [".psd"],                           "in_folder": "",   "name_has": ""},
            {"dest": "01_Assets/Audio/Music",                  "exts": [".mp3"],                           "in_folder": "",   "name_has": ""},
            {"dest": "01_Assets/Audio/SFX",                    "exts": [".wav", ".pkf"],                   "in_folder": "fx", "name_has": ""},
            {"dest": "01_Assets/Images/References",            "exts": [".png", ".jpg", ".jpeg", ".webp"], "in_folder": "",   "name_has": ""},
            {"dest": "03_Exports/Finals",                      "exts": [".mp4", ".mov", ".avi"],           "in_folder": "",   "name_has": "final"},
            {"dest": "03_Exports/Drafts",                      "exts": [".mp4", ".mov", ".avi"],           "in_folder": "",   "name_has": ""},
        ],
        "folder_moves": [
            ("adobe after effects auto-save", "00_Project_Files/AfterEffects/ae_cache"),
        ],
    },

    "3d": {
        "label":    "3D Animation",
        "subtitle": "Blender  ·  AE  ·  Illustrator",
        "structure": [
            "00_Project_Files/AfterEffects/projects",
            "00_Project_Files/AfterEffects/ae_cache",
            "00_Project_Files/Blender/scenes",
            "00_Project_Files/Blender/textures",
            "00_Project_Files/Illustrator",
            "00_Project_Files/Photoshop",
            "01_Assets/Audio/Music",
            "01_Assets/Audio/SFX",
            "01_Assets/Audio/VO",
            "01_Assets/Footage/Raw",
            "01_Assets/Footage/Proxies",
            "01_Assets/Images/References",
            "01_Assets/Images/Textures",
            "01_Assets/HDRI",
            "01_Assets/Fonts",
            "02_Renders/Blender/EXR",
            "02_Renders/Blender/Preview",
            "02_Renders/Blender/SEQ",
            "02_Renders/AE_Previews",
            "03_Exports/Drafts/v001",
            "03_Exports/Finals",
            "04_Docs/Brief",
            "04_Docs/References",
            "04_Docs/Feedback",
            "05_Handoff",
        ],
        "rules": [
            {"dest": "00_Project_Files/AfterEffects/projects", "exts": [".aep"],                             "in_folder": "",        "name_has": ""},
            {"dest": "00_Project_Files/Blender/scenes",        "exts": [".blend", ".blend1", ".fspy"],       "in_folder": "",        "name_has": ""},
            {"dest": "00_Project_Files/Illustrator",           "exts": [".ai"],                              "in_folder": "",        "name_has": ""},
            {"dest": "00_Project_Files/Photoshop",             "exts": [".psd"],                             "in_folder": "",        "name_has": ""},
            {"dest": "02_Renders/Blender",                     "exts": [".png", ".exr"],                     "in_folder": "render",  "name_has": ""},
            {"dest": "01_Assets/Audio/Music",                  "exts": [".mp3"],                             "in_folder": "",        "name_has": ""},
            {"dest": "01_Assets/Audio/SFX",                    "exts": [".wav"],                             "in_folder": "fx",      "name_has": ""},
            {"dest": "01_Assets/Images/Textures",              "exts": [".png", ".jpg"],                     "in_folder": "texture", "name_has": ""},
            {"dest": "01_Assets/Images/References",            "exts": [".png", ".jpg", ".jpeg", ".webp"],   "in_folder": "",        "name_has": ""},
            {"dest": "03_Exports/Finals",                      "exts": [".mp4", ".mov", ".avi"],             "in_folder": "",        "name_has": "final"},
            {"dest": "03_Exports/Drafts",                      "exts": [".mp4", ".mov", ".avi"],             "in_folder": "",        "name_has": ""},
        ],
        "folder_moves": [
            ("adobe after effects auto-save", "00_Project_Files/AfterEffects/ae_cache"),
        ],
    },

    "edit": {
        "label":    "Video Editing",
        "subtitle": "DaVinci Resolve  ·  Audition  ·  AE",
        "structure": [
            "00_Project_Files/DaVinci",
            "00_Project_Files/AfterEffects",
            "00_Project_Files/Audition",
            "01_Media/Footage/Raw",
            "01_Media/Footage/Proxies",
            "01_Media/Audio/Music",
            "01_Media/Audio/SFX",
            "01_Media/Audio/VO",
            "01_Media/Audio/Stems",
            "01_Media/Graphics",
            "01_Media/Stills",
            "02_Cache/DaVinci_Cache",
            "02_Cache/Optimized_Media",
            "03_Exports/Drafts/v001",
            "03_Exports/Finals",
            "04_Audio_Mix/Sessions",
            "04_Audio_Mix/Stems",
            "04_Audio_Mix/Finals",
            "05_Docs/Brief",
            "05_Docs/Scripts",
            "05_Docs/Feedback",
            "06_From_Animation",
        ],
        "rules": [
            {"dest": "00_Project_Files/DaVinci",      "exts": [".drp", ".drt"],                          "in_folder": "",    "name_has": ""},
            {"dest": "00_Project_Files/AfterEffects", "exts": [".aep"],                                  "in_folder": "",    "name_has": ""},
            {"dest": "00_Project_Files/Audition",     "exts": [".sesx"],                                 "in_folder": "",    "name_has": ""},
            {"dest": "01_Media/Audio/Music",          "exts": [".mp3"],                                  "in_folder": "",    "name_has": ""},
            {"dest": "01_Media/Audio/SFX",            "exts": [".wav"],                                  "in_folder": "fx",  "name_has": ""},
            {"dest": "01_Media/Audio/VO",             "exts": [".wav", ".pkf"],                          "in_folder": "",    "name_has": "vo"},
            {"dest": "01_Media/Audio/VO",             "exts": [".wav", ".pkf"],                          "in_folder": "",    "name_has": "voice"},
            {"dest": "01_Media/Footage/Raw",          "exts": [".mp4", ".mov", ".mxf"],                  "in_folder": "raw", "name_has": ""},
            {"dest": "01_Media/Stills",               "exts": [".png", ".jpg", ".jpeg"],                 "in_folder": "",    "name_has": ""},
            {"dest": "03_Exports/Finals",             "exts": [".mp4", ".mov"],                          "in_folder": "",    "name_has": "final"},
            {"dest": "03_Exports/Drafts",             "exts": [".mp4", ".mov", ".avi"],                  "in_folder": "",    "name_has": ""},
        ],
        "folder_moves": [],
    },

    "gfx": {
        "label":    "Graphic Design",
        "subtitle": "Illustrator  ·  Photoshop",
        "structure": [
            "01_Assets/Illustrator",
            "01_Assets/Photoshop",
            "01_Assets/Images/References",
            "01_Assets/Images/Stock",
            "01_Assets/Fonts",
            "01_Assets/Icons",
            "01_Assets/Brand/Logos",
            "01_Assets/Brand/Swatches",
            "02_Exports/Print",
            "02_Exports/Digital/Web",
            "02_Exports/Digital/Social",
            "02_Exports/Brand",
            "03_Docs/Brief",
            "03_Docs/References",
            "03_Docs/Feedback",
            "04_Handoff",
        ],
        "rules": [
            {"dest": "01_Assets/Illustrator",         "exts": [".ai"],                               "in_folder": "", "name_has": ""},
            {"dest": "01_Assets/Photoshop",           "exts": [".psd"],                              "in_folder": "", "name_has": ""},
            {"dest": "02_Exports/Brand",              "exts": [".svg", ".pdf", ".png"],              "in_folder": "", "name_has": "logo"},
            {"dest": "02_Exports/Digital/Social",     "exts": [".png", ".jpg", ".jpeg"],             "in_folder": "", "name_has": "social"},
            {"dest": "02_Exports/Digital/Web",        "exts": [".png", ".jpg", ".jpeg", ".svg"],     "in_folder": "", "name_has": "web"},
            {"dest": "02_Exports/Print",              "exts": [".pdf"],                              "in_folder": "", "name_has": "print"},
            {"dest": "03_Docs/Brief",                 "exts": [".pdf"],                              "in_folder": "", "name_has": "brief"},
            {"dest": "03_Docs/References",            "exts": [".pdf"],                              "in_folder": "", "name_has": ""},
            {"dest": "01_Assets/Icons",               "exts": [".svg"],                              "in_folder": "", "name_has": ""},
            {"dest": "01_Assets/Fonts",               "exts": [".ttf", ".otf", ".woff", ".woff2"],  "in_folder": "", "name_has": ""},
            {"dest": "01_Assets/Images/References",   "exts": [".png", ".jpg", ".jpeg", ".webp"],   "in_folder": "", "name_has": ""},
        ],
        "folder_moves": [],
    },

    "vfx": {
        "label":    "VFX Compositing",
        "subtitle": "All tools combined",
        "structure": [
            "00_Project_Files/AfterEffects/projects",
            "00_Project_Files/AfterEffects/ae_cache",
            "00_Project_Files/Blender/scenes",
            "00_Project_Files/Blender/textures",
            "00_Project_Files/DaVinci",
            "00_Project_Files/Illustrator",
            "00_Project_Files/Photoshop",
            "01_Assets/Audio/Music",
            "01_Assets/Audio/SFX",
            "01_Assets/Audio/VO",
            "01_Assets/Footage/Raw",
            "01_Assets/Footage/Greenscreen",
            "01_Assets/Images/References",
            "01_Assets/Images/Textures",
            "01_Assets/HDRI",
            "01_Assets/Fonts",
            "02_Renders/Blender/EXR",
            "02_Renders/Blender/Preview",
            "02_Renders/Blender/SEQ",
            "02_Renders/AE_Previews",
            "02_Renders/VFX_Passes",
            "03_Exports/Drafts/v001",
            "03_Exports/Finals",
            "04_Docs/Brief",
            "04_Docs/References",
            "04_Docs/Feedback",
            "05_Handoff",
        ],
        "rules": [
            {"dest": "00_Project_Files/AfterEffects/projects", "exts": [".aep"],                           "in_folder": "",        "name_has": ""},
            {"dest": "00_Project_Files/Blender/scenes",        "exts": [".blend", ".blend1", ".fspy"],     "in_folder": "",        "name_has": ""},
            {"dest": "00_Project_Files/DaVinci",               "exts": [".drp", ".drt"],                   "in_folder": "",        "name_has": ""},
            {"dest": "00_Project_Files/Illustrator",           "exts": [".ai"],                            "in_folder": "",        "name_has": ""},
            {"dest": "00_Project_Files/Photoshop",             "exts": [".psd"],                           "in_folder": "",        "name_has": ""},
            {"dest": "02_Renders/Blender",                     "exts": [".png", ".exr"],                   "in_folder": "render",  "name_has": ""},
            {"dest": "02_Renders/VFX_Passes",                  "exts": [".exr", ".png"],                   "in_folder": "pass",    "name_has": ""},
            {"dest": "01_Assets/Footage/Greenscreen",          "exts": [".mp4", ".mov"],                   "in_folder": "",        "name_has": "green"},
            {"dest": "01_Assets/Footage/Raw",                  "exts": [".mp4", ".mov", ".mxf"],           "in_folder": "raw",     "name_has": ""},
            {"dest": "01_Assets/Audio/Music",                  "exts": [".mp3"],                           "in_folder": "",        "name_has": ""},
            {"dest": "01_Assets/Audio/SFX",                    "exts": [".wav"],                           "in_folder": "fx",      "name_has": ""},
            {"dest": "01_Assets/Images/Textures",              "exts": [".png", ".jpg"],                   "in_folder": "texture", "name_has": ""},
            {"dest": "01_Assets/Images/References",            "exts": [".png", ".jpg", ".jpeg", ".webp"], "in_folder": "",        "name_has": ""},
            {"dest": "03_Exports/Finals",                      "exts": [".mp4", ".mov", ".avi"],           "in_folder": "",        "name_has": "final"},
            {"dest": "03_Exports/Drafts",                      "exts": [".mp4", ".mov", ".avi"],           "in_folder": "",        "name_has": ""},
        ],
        "folder_moves": [
            ("adobe after effects auto-save", "00_Project_Files/AfterEffects/ae_cache"),
        ],
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# ENGINE
# ─────────────────────────────────────────────────────────────────────────────

import re as _re
_SEQ_PATTERN = _re.compile(r'^\d{2,}\.(?:png|exr|jpg|jpeg|tiff|tga|dpx)$', _re.IGNORECASE)

def is_sequence_folder(folder: Path) -> bool:
    """True if folder contains a numbered image sequence (e.g. 0001.png, 0002.png)."""
    try:
        files = [f for f in folder.iterdir() if f.is_file()]
    except PermissionError:
        return False
    if len(files) < 3:
        return False
    numbered = [f for f in files if _SEQ_PATTERN.match(f.name)]
    return len(numbered) / len(files) >= 0.7


def find_sequence_folders(root: Path, dest_roots: set) -> list[Path]:
    """Return all image sequence folders not already inside our destination structure."""
    result = []
    for folder in sorted(root.rglob("*")):
        if not folder.is_dir():
            continue
        if folder.relative_to(root).parts[0] in dest_roots:
            continue
        if is_sequence_folder(folder):
            result.append(folder)
    return result


def safe_dest(path: Path) -> Path:
    """Return path unchanged if it doesn't exist, otherwise add _01, _02… until clear."""
    if not path.exists():
        return path
    counter = 1
    while True:
        candidate = path.with_stem(f"{path.stem}_{counter:02d}")
        if not candidate.exists():
            return candidate
        counter += 1


def matches(file: Path, rule: dict) -> bool:
    name_lower    = file.name.lower()
    parents_lower = " ".join(p.name.lower() for p in file.parents)
    if rule["exts"] and file.suffix.lower() not in rule["exts"]:
        return False
    if rule["in_folder"] and rule["in_folder"].lower() not in parents_lower:
        return False
    if rule["name_has"] and rule["name_has"].lower() not in name_lower:
        return False
    return True


def create_structure(root: Path, project_type: str, dry_run: bool, log):
    folders = TYPES[project_type]["structure"]
    log(f"Creating {len(folders)} folders...\n")
    for rel in folders:
        path = root / Path(rel)
        if not dry_run:
            path.mkdir(parents=True, exist_ok=True)
        log(f"  + {rel}")
    log(f"\n{'Done.' if not dry_run else 'Preview complete — no folders were created.'}")


def reorganise(root: Path, project_type: str, dry_run: bool, log):
    cfg   = TYPES[project_type]
    rules = cfg["rules"]

    dest_roots = {Path(v).parts[0] for v in cfg["structure"]}

    # Scan first so we can report totals upfront
    all_files = [
        f for f in sorted(root.rglob("*"))
        if f.is_file() and f.relative_to(root).parts[0] not in dest_roots
    ]
    seq_folders_preview = find_sequence_folders(root, dest_roots)
    seq_files_preview   = {f for seq in seq_folders_preview for f in seq.rglob("*") if f.is_file()}
    non_seq_files       = [f for f in all_files if f not in seq_files_preview]
    matched_files       = [f for f in non_seq_files if any(matches(f, r) for r in rules)]
    unmatched_files     = [f for f in non_seq_files if f not in matched_files]

    seq_frame_count = len(seq_files_preview)
    log(f"Found {len(all_files)} files total")
    if seq_folders_preview:
        log(f"  {len(seq_folders_preview)} image sequence folder(s)  ({seq_frame_count} frames — moved as units)")
    log(f"  {len(matched_files)} regular files will be sorted")
    if unmatched_files:
        log(f"  {len(unmatched_files)} files will be left in place")
    log("")

    # Create destination folders
    log(f"Creating {len(cfg['structure'])} destination folders...")
    for rel in cfg["structure"]:
        if not dry_run:
            (root / Path(rel)).mkdir(parents=True, exist_ok=True)

    moves = []  # undo log

    # Move whole folders first
    if cfg["folder_moves"]:
        log("")
        for name_frag, dest_rel in cfg["folder_moves"]:
            for folder in sorted(root.rglob("*")):
                if folder.is_dir() and name_frag in folder.name.lower():
                    dest = root / dest_rel / folder.name
                    log(f"  {'[preview] ' if dry_run else ''}FOLDER  {folder.name}  →  {dest_rel}/")
                    if not dry_run:
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        if dest.exists():
                            for item in folder.iterdir():
                                actual = safe_dest(dest / item.name)
                                moves.append({"from": str(item), "to": str(actual)})
                                shutil.move(str(item), actual)
                            shutil.rmtree(str(folder))
                        else:
                            moves.append({"from": str(folder), "to": str(dest)})
                            shutil.move(str(folder), dest)

    # Move image sequence folders as units
    seq_folders = find_sequence_folders(root, dest_roots)
    seq_files   = set()
    if seq_folders:
        log(f"\nFound {len(seq_folders)} image sequence folder(s) — moving as units...\n")
        renders_root = root / "02_Renders" / "Blender" / "SEQ"
        for seq in seq_folders:
            parent_name = seq.parent.name
            if seq.parent == root or seq.parent.relative_to(root).parts[0] in dest_roots:
                dest_seq = renders_root / seq.name
            else:
                dest_seq = renders_root / parent_name / seq.name
            log(f"  {'[preview] ' if dry_run else ''}SEQ  {seq.relative_to(root)}  →  {dest_seq.relative_to(root)}/")
            if not dry_run:
                dest_seq.parent.mkdir(parents=True, exist_ok=True)
                if dest_seq.exists():
                    for item in seq.iterdir():
                        actual = safe_dest(dest_seq / item.name)
                        moves.append({"from": str(item), "to": str(actual)})
                        shutil.move(str(item), actual)
                    shutil.rmtree(str(seq))
                else:
                    moves.append({"from": str(seq), "to": str(dest_seq)})
                    shutil.move(str(seq), dest_seq)
            for f in seq.rglob("*"):
                if f.is_file():
                    seq_files.add(f)

    # Walk individual files and apply rules
    log(f"\nSorting {len(matched_files)} files...\n")
    moved, skipped = 0, []
    for file in sorted(root.rglob("*")):
        if not file.is_file():
            continue
        if file.relative_to(root).parts[0] in dest_roots:
            continue
        if file in seq_files:
            continue

        for rule in rules:
            if matches(file, rule):
                dest = root / rule["dest"] / file.name
                if not dry_run:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest = safe_dest(dest)
                    moves.append({"from": str(file), "to": str(dest)})
                    shutil.move(str(file), dest)
                log(f"  {'[preview] ' if dry_run else ''}{file.name}  →  {rule['dest']}/")
                moved += 1
                break
        else:
            skipped.append(str(file.relative_to(root)))

    # Remove empty folders
    if not dry_run:
        removed_dirs = 0
        for folder in sorted(root.rglob("*"), reverse=True):
            if folder.is_dir():
                try:
                    folder.rmdir()
                    removed_dirs += 1
                except OSError:
                    pass
        # Save undo log
        undo_file = root / ".reorganise_undo.json"
        undo_file.write_text(json.dumps(moves, indent=2), encoding="utf-8")

    log(f"\n── Summary {'(preview) ' if dry_run else ''}───────────────────────")
    log(f"  {'Would move' if dry_run else 'Moved'} : {moved} files")
    if not dry_run:
        log(f"  Cleaned up : {removed_dirs} empty folders")
    if skipped:
        log(f"  Left alone : {len(skipped)} files (no matching rule)")
        for s in skipped:
            log(f"    {s}")
    log(f"\n{'Done.' if not dry_run else 'Preview complete — no files were moved.'}")


def undo_reorganise(root: Path, log):
    undo_file = root / ".reorganise_undo.json"
    if not undo_file.exists():
        log("No undo history found for this folder.")
        return
    moves = json.loads(undo_file.read_text(encoding="utf-8"))
    log(f"Reversing {len(moves)} move(s)...\n")
    errors = 0
    for move in reversed(moves):
        src = Path(move["to"])
        dst = Path(move["from"])
        if not src.exists():
            log(f"  SKIP (already missing): {src.name}")
            errors += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            dst = dst.with_stem(dst.stem + "_restored")
        shutil.move(str(src), dst)
        log(f"  {src.name}  →  {dst.parent.name}/")
    # Clean up empty destination folders left behind
    for folder in sorted(root.rglob("*"), reverse=True):
        if folder.is_dir():
            try:
                folder.rmdir()
            except OSError:
                pass
    undo_file.unlink()
    log(f"\nUndo complete. {len(moves) - errors} item(s) restored.")


# ─────────────────────────────────────────────────────────────────────────────
# GUI
# ─────────────────────────────────────────────────────────────────────────────

def run_gui(pre_folder=""):
    import tkinter as tk
    from tkinter import filedialog, scrolledtext

    BG     = "#1e1e2e"
    CARD   = "#2a2a3d"
    ACCENT = "#7c6af7"
    TEXT   = "#e0e0f0"
    MUTED  = "#7a7a9a"

    win = tk.Tk()
    win.title("Project Folder Tool")
    win.configure(bg=BG)
    win.resizable(False, False)

    type_var   = tk.StringVar(value="2d")
    mode_var   = tk.StringVar(value="create")
    folder_var = tk.StringVar(value=pre_folder)

    # ── Layout helpers ───────────────────────────────────────────────────────
    def section_label(text):
        tk.Label(win, text=text, bg=BG, fg=MUTED,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=16, pady=(10, 2))

    def card_frame():
        f = tk.Frame(win, bg=CARD)
        f.pack(fill="x", padx=12, pady=0)
        return f

    # ── Header ───────────────────────────────────────────────────────────────
    tk.Frame(win, bg=ACCENT, height=4).pack(fill="x")
    tk.Label(win, text="Project Folder Tool", bg=BG, fg=TEXT,
             font=("Segoe UI", 13, "bold")).pack(pady=(14, 4))

    # ── Project type ─────────────────────────────────────────────────────────
    section_label("PROJECT TYPE")
    type_card = card_frame()

    for key, title, sub in [
        ("2d",   "2D Motion Graphics", "AE  ·  Illustrator  ·  Photoshop"),
        ("3d",   "3D Animation",       "Blender  ·  AE  ·  Illustrator"),
        ("edit", "Video Editing",      "DaVinci Resolve  ·  Audition  ·  AE"),
        ("gfx",  "Graphic Design",     "Illustrator  ·  Photoshop"),
        ("vfx",  "VFX Compositing",    "All tools combined"),
    ]:
        row = tk.Frame(type_card, bg=CARD)
        row.pack(fill="x", padx=8, pady=3)
        tk.Radiobutton(row, variable=type_var, value=key,
                       bg=CARD, fg=TEXT, selectcolor=ACCENT,
                       activebackground=CARD, activeforeground=TEXT,
                       cursor="hand2").pack(side="left")
        tk.Label(row, text=title, bg=CARD, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(side="left")
        tk.Label(row, text=f"   {sub}", bg=CARD, fg=MUTED,
                 font=("Segoe UI", 9)).pack(side="left")

    tk.Frame(type_card, bg=CARD, height=6).pack()

    # ── Mode ─────────────────────────────────────────────────────────────────
    section_label("MODE")
    mode_card = card_frame()

    for val, title in [
        ("create", "Create new project structure"),
        ("reorg",  "Reorganise existing folder"),
    ]:
        row = tk.Frame(mode_card, bg=CARD)
        row.pack(fill="x", padx=8, pady=3)
        tk.Radiobutton(row, variable=mode_var, value=val,
                       bg=CARD, fg=TEXT, selectcolor=ACCENT,
                       activebackground=CARD, activeforeground=TEXT,
                       cursor="hand2").pack(side="left")
        tk.Label(row, text=title, bg=CARD, fg=TEXT,
                 font=("Segoe UI", 10)).pack(side="left")

    tk.Frame(mode_card, bg=CARD, height=6).pack()

    # ── Folder picker ────────────────────────────────────────────────────────
    section_label("FOLDER")
    folder_card = card_frame()
    folder_row  = tk.Frame(folder_card, bg=CARD)
    folder_row.pack(fill="x", padx=8, pady=8)

    entry = tk.Entry(folder_row, textvariable=folder_var, width=46,
                     bg="#13131f", fg=TEXT, insertbackground=TEXT,
                     font=("Segoe UI", 9), relief="flat", bd=4)
    entry.pack(side="left", fill="x", expand=True)

    def browse():
        chosen = filedialog.askdirectory(title="Select project folder")
        if chosen:
            folder_var.set(chosen)

    tk.Button(folder_row, text="Browse", command=browse,
              bg=ACCENT, fg="white", relief="flat", cursor="hand2",
              font=("Segoe UI", 9), padx=10, pady=2).pack(side="left", padx=(8, 0))

    # ── Output ───────────────────────────────────────────────────────────────
    out = scrolledtext.ScrolledText(win, height=14, width=62,
                                    bg="#13131f", fg=TEXT,
                                    font=("Consolas", 9), relief="flat",
                                    state="disabled")
    out.pack(fill="x", padx=12, pady=10)

    def log(msg):
        out.config(state="normal")
        out.insert("end", msg + "\n")
        out.see("end")
        out.config(state="disabled")
        win.update_idletasks()

    def clear_log():
        out.config(state="normal")
        out.delete("1.0", "end")
        out.config(state="disabled")

    def show_tree(ptype):
        """Show the folder tree for the selected project type in the output area."""
        clear_log()
        cfg = TYPES[ptype]
        log(f"{cfg['label']}  —  {cfg['subtitle']}\n")
        seen = []
        for rel in cfg["structure"]:
            parts = Path(rel).parts
            for depth, _ in enumerate(parts):
                partial = parts[:depth + 1]
                if partial not in seen:
                    seen.append(partial)
                    indent = "  " * depth
                    prefix = "└─ " if depth > 0 else ""
                    log(f"{indent}{prefix}📁 {partial[-1]}/")

    # Show tree on type selection change
    def on_type_change(*_):
        show_tree(type_var.get())

    type_var.trace_add("write", on_type_change)
    show_tree("2d")  # default preview

    # ── Buttons ──────────────────────────────────────────────────────────────
    btn_row = tk.Frame(win, bg=BG)
    btn_row.pack(pady=(0, 14))

    undo_btn = None  # forward reference

    def refresh_undo_btn(*_):
        folder = folder_var.get().strip()
        has_log = folder and (Path(folder) / ".reorganise_undo.json").exists()
        undo_btn.config(state="normal" if has_log else "disabled",
                        fg=TEXT if has_log else "#555570")

    def run(dry):
        folder = folder_var.get().strip()
        if not folder:
            clear_log()
            log("Please select a folder first.")
            return
        path = Path(folder)
        if not path.exists():
            clear_log()
            log(f"Folder not found:\n  {folder}")
            return
        clear_log()
        ptype = type_var.get()
        mode  = mode_var.get()
        log(f"{'[DRY RUN]  ' if dry else ''}"
            f"{'Creating structure' if mode == 'create' else 'Reorganising'}  —  "
            f"{TYPES[ptype]['label']}")
        log(f"Folder: {folder}\n")

        def task():
            try:
                if mode == "create":
                    create_structure(path, ptype, dry, log)
                else:
                    reorganise(path, ptype, dry, log)
                if not dry and mode == "create":
                    log("\n── Folder tree created ──────────────────")
                    show_tree(ptype)
            except Exception as e:
                log(f"\nERROR: {e}")
            finally:
                win.after(0, refresh_undo_btn)

        threading.Thread(target=task, daemon=True).start()

    def run_undo():
        folder = folder_var.get().strip()
        if not folder:
            return
        path = Path(folder)
        clear_log()
        log(f"Undoing last reorganisation in:\n{folder}\n")

        def task():
            try:
                undo_reorganise(path, log)
            except Exception as e:
                log(f"\nERROR: {e}")
            finally:
                win.after(0, refresh_undo_btn)

        threading.Thread(target=task, daemon=True).start()

    tk.Button(btn_row, text="Preview",
              command=lambda: run(dry=True),
              bg=CARD, fg=TEXT, relief="flat", cursor="hand2",
              font=("Segoe UI", 10), padx=18, pady=6).pack(side="left", padx=(0, 10))

    tk.Button(btn_row, text="Run",
              command=lambda: run(dry=False),
              bg=ACCENT, fg="white", relief="flat", cursor="hand2",
              font=("Segoe UI", 10, "bold"), padx=28, pady=6).pack(side="left", padx=(0, 10))

    undo_btn = tk.Button(btn_row, text="Undo",
                         command=run_undo,
                         bg=CARD, fg="#555570", relief="flat", cursor="hand2",
                         font=("Segoe UI", 10), padx=18, pady=6, state="disabled")
    undo_btn.pack(side="left")

    folder_var.trace_add("write", refresh_undo_btn)
    refresh_undo_btn()  # set initial state

    win.mainloop()


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    positional = [a for a in sys.argv[1:] if not a.startswith("--")]
    pre_folder = positional[0] if positional else ""
    run_gui(pre_folder=pre_folder)
