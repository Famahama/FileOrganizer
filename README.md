# File Organizer — Progresif Media

A GUI tool for creating and reorganising project folders. Supports 5 project types across animation, editing, and design.

---

## For Team Members

You only need one file: **`00.FileOrganizer.bat`**

1. Drop `00.FileOrganizer.bat` into your project folder
2. Double-click it
3. The tool opens with your folder pre-filled
4. Pick your project type and mode, then hit **Preview** or **Run**

The tool updates automatically every time you open it — no need to download new versions.

> Requires Python to be installed on your machine. See [Installing Python](#installing-python) below if you haven't done this yet.

---

## Modes

| Mode | What it does |
|---|---|
| **Create new project structure** | Builds empty folders in the selected directory |
| **Reorganise existing folder** | Sorts existing files into the correct folders |

Run **Preview** first to see what will move without touching anything. Then **Run** to apply. Use **Undo** if you change your mind — it reverses the last reorganisation.

---

## Project Types

### 2D Motion Graphics
*AE · Illustrator · Photoshop*
```
00_Project_Files/
  └─ AfterEffects/
    └─ projects/
    └─ ae_cache/
  └─ Illustrator/
  └─ Photoshop/
01_Assets/
  └─ Audio/
    └─ Music/
    └─ SFX/
  └─ Footage/
    └─ Raw/
    └─ Proxies/
  └─ Images/
    └─ References/
  └─ Fonts/
02_Renders/
  └─ AE_Previews/
03_Exports/
  └─ Drafts/
    └─ v001/
  └─ Finals/
04_Docs/
  └─ Brief/
  └─ References/
  └─ Feedback/
05_Handoff/
```

---

### 3D Animation
*Blender · AE · Illustrator*
```
00_Project_Files/
  └─ AfterEffects/
    └─ projects/
    └─ ae_cache/
  └─ Blender/
    └─ scenes/
    └─ textures/
  └─ Illustrator/
  └─ Photoshop/
01_Assets/
  └─ Audio/
    └─ Music/
    └─ SFX/
    └─ VO/
  └─ Footage/
    └─ Raw/
    └─ Proxies/
  └─ Images/
    └─ References/
    └─ Textures/
  └─ HDRI/
  └─ Fonts/
02_Renders/
  └─ Blender/
    └─ EXR/
    └─ Preview/
    └─ SEQ/
  └─ AE_Previews/
03_Exports/
  └─ Drafts/
    └─ v001/
  └─ Finals/
04_Docs/
  └─ Brief/
  └─ References/
  └─ Feedback/
05_Handoff/
```

---

### Video Editing
*DaVinci Resolve · Audition · AE*
```
00_Project_Files/
  └─ DaVinci/
  └─ AfterEffects/
  └─ Audition/
01_Media/
  └─ Footage/
    └─ Raw/
    └─ Proxies/
  └─ Audio/
    └─ Music/
    └─ SFX/
    └─ VO/
    └─ Stems/
  └─ Graphics/
  └─ Stills/
02_Cache/
  └─ DaVinci_Cache/
  └─ Optimized_Media/
03_Exports/
  └─ Drafts/
    └─ v001/
  └─ Finals/
04_Audio_Mix/
  └─ Sessions/
  └─ Stems/
  └─ Finals/
05_Docs/
  └─ Brief/
  └─ Scripts/
  └─ Feedback/
06_From_Animation/
```

---

### Graphic Design
*Illustrator · Photoshop*
```
00_Project_Files/
  └─ Illustrator/
  └─ Photoshop/
01_Assets/
  └─ Illustrator/
  └─ Photoshop/
  └─ Images/
    └─ References/
    └─ Stock/
  └─ Fonts/
  └─ Icons/
  └─ Brand/
    └─ Logos/
    └─ Swatches/
02_Exports/
  └─ Print/
  └─ Digital/
    └─ Web/
    └─ Social/
  └─ Brand/
03_Docs/
  └─ Brief/
  └─ References/
  └─ Feedback/
04_Handoff/
```

> **Versioned files** (e.g. `poster_v_01.ai`, `logo_v-03.psd`) go to `00_Project_Files/`. All other `.ai` and `.psd` files go to `01_Assets/`.

---

### VFX Compositing
*All tools combined*
```
00_Project_Files/
  └─ AfterEffects/
    └─ projects/
    └─ ae_cache/
  └─ Blender/
    └─ scenes/
    └─ textures/
  └─ DaVinci/
  └─ Illustrator/
  └─ Photoshop/
01_Assets/
  └─ Audio/
    └─ Music/
    └─ SFX/
    └─ VO/
  └─ Footage/
    └─ Raw/
    └─ Greenscreen/
  └─ Images/
    └─ References/
    └─ Textures/
  └─ HDRI/
  └─ Fonts/
02_Renders/
  └─ Blender/
    └─ EXR/
    └─ Preview/
    └─ SEQ/
  └─ AE_Previews/
  └─ VFX_Passes/
03_Exports/
  └─ Drafts/
    └─ v001/
  └─ Finals/
04_Docs/
  └─ Brief/
  └─ References/
  └─ Feedback/
05_Handoff/
```

---

## File Sorting Rules

When using **Reorganise**, files are matched by extension and filename. First match wins.

| Extension | Condition | Goes to |
|---|---|---|
| `.aep` | — | `00_Project_Files/AfterEffects/projects/` |
| `.blend` `.blend1` `.fspy` | — | `00_Project_Files/Blender/scenes/` |
| `.ai` | — | `00_Project_Files/Illustrator/` |
| `.psd` | — | `00_Project_Files/Photoshop/` |
| `.drp` `.drt` | — | `00_Project_Files/DaVinci/` |
| `.sesx` | — | `00_Project_Files/Audition/` |
| `.mp4` `.mov` `.avi` | name has `final` | `03_Exports/Finals/` |
| `.mp4` `.mov` `.avi` | — | `03_Exports/Drafts/` |
| `.mp3` | — | `01_Assets/Audio/Music/` |
| `.wav` | name has `vo` or `voice` | `01_Assets/Audio/VO/` |
| `.wav` | in a folder named `fx` | `01_Assets/Audio/SFX/` |
| `.pdf` | name has `logo` | `02_Exports/Brand/` *(GFX only)* |
| `.pdf` | name has `print` | `02_Exports/Print/` *(GFX only)* |
| `.pdf` | name has `brief` | `03_Docs/Brief/` |
| `.pdf` | — | `03_Docs/References/` |
| `.svg` | name has `logo` or `web` | `02_Exports/Brand/` or `Digital/Web/` |
| `.svg` | — | `01_Assets/Icons/` |
| `.ttf` `.otf` `.woff` | — | `01_Assets/Fonts/` |
| `.png` `.jpg` `.jpeg` | in a folder named `texture` | `01_Assets/Images/Textures/` |
| `.png` `.jpg` `.jpeg` | — | `01_Assets/Images/References/` |
| Numbered image sequence folder | ≥70% numbered files | `02_Renders/Blender/SEQ/` *(moved as a unit)* |

Files that don't match any rule are left in place and listed in the summary.

---

## Installing Python

Python only needs to be installed once per machine.

1. Go to **[python.org/downloads](https://www.python.org/downloads/)**
2. Click the **Download Python** button (latest version)
3. Run the installer
4. **Important:** On the first screen, tick the box that says **"Add python.exe to PATH"** before clicking Install

   ![Add to PATH checkbox must be ticked](https://www.python.org/static/img/python-logo.png)

   > If you skip this step, the tool won't open. You'll need to uninstall and reinstall Python with the box ticked.

5. Click **Install Now** and wait for it to finish
6. Click **Close**

**To verify it worked:**
- Press `Windows + R`, type `cmd`, press Enter
- Type `python --version` and press Enter
- You should see something like `Python 3.x.x`

If you see an error instead, Python was not added to PATH — uninstall it from **Control Panel → Programs** and reinstall with the checkbox ticked.

---

## Updating the Tool (Admin)

Make changes to `reorganise.py` on your machine, then push:

```
git add reorganise.py
git commit -m "describe what changed"
git push
```

The team gets the update automatically next time they open `00.FileOrganizer.bat`.
