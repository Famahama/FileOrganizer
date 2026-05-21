# File Organizer

A GUI tool for creating and reorganising project folders for Graphic Design projects.

---

## For Team Members

You only need one file: **`00.FileOrganizer.bat`**

1. Drop `00.FileOrganizer.bat` into your project folder
2. Double-click it
3. The tool opens with your folder pre-filled
4. Pick your mode, then hit **Preview** or **Run**

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

## Folder Structure

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

## File Sorting Rules

When using **Reorganise**, files are matched by extension and filename. First match wins.

| Extension | Condition | Goes to |
|---|---|---|
| `.ai` | name has `v_00`–`v_99` or `v-00`–`v-99` | `00_Project_Files/Illustrator/` |
| `.psd` | name has `v_00`–`v_99` or `v-00`–`v-99` | `00_Project_Files/Photoshop/` |
| `.ai` | — | `01_Assets/Illustrator/` |
| `.psd` | — | `01_Assets/Photoshop/` |
| `.svg` `.pdf` `.png` | name has `logo` | `02_Exports/Brand/` |
| `.png` `.jpg` `.jpeg` | name has `social` | `02_Exports/Digital/Social/` |
| `.png` `.jpg` `.jpeg` `.svg` | name has `web` | `02_Exports/Digital/Web/` |
| `.pdf` | name has `print` | `02_Exports/Print/` |
| `.pdf` | name has `brief` | `03_Docs/Brief/` |
| `.pdf` | — | `03_Docs/References/` |
| `.svg` | — | `01_Assets/Icons/` |
| `.ttf` `.otf` `.woff` `.woff2` | — | `01_Assets/Fonts/` |
| `.png` `.jpg` `.jpeg` `.webp` | — | `01_Assets/Images/References/` |

Files that don't match any rule are left in place and listed in the summary.

---

## Installing Python

Python only needs to be installed once per machine.

### Option 1 — Command line (recommended)

This installs Python and automatically adds it to PATH in one step.

#### Windows 11

Winget comes pre-installed on Windows 11.

**Step 1.** Right-click the **Start button** and select **Terminal**

**Step 2.** Paste and run this command:

```cmd
winget install -e --id Python.Python.3 --override "PrependPath=1 Include_pip=1 /quiet"
```

**Step 3.** Wait for it to finish, then close and reopen Terminal

**Step 4.** Type `python --version` to confirm — you should see `Python 3.x.x`

#### Windows 10

Winget may not be pre-installed. If the command above gives an error, install winget first from the [Microsoft Store](https://www.microsoft.com/store/productId/9NBLGGH4NNS1), then repeat the steps above.

**Step 1.** Press `Windows + R`, type `cmd`, and press Enter

**Step 2.** Paste and run this command:

```cmd
winget install -e --id Python.Python.3 --override "PrependPath=1 Include_pip=1 /quiet"
```

**Step 3.** Wait for it to finish, then close and reopen CMD

**Step 4.** Type `python --version` to confirm — you should see `Python 3.x.x`

---

### Option 2 — Manual installer

1. Go to **[python.org/downloads](https://www.python.org/downloads/)** and download the latest version
2. Run the installer
3. **Important:** Tick **"Add python.exe to PATH"** on the first screen before clicking Install Now

   > If you miss this step, the tool won't open. Uninstall Python from **Control Panel → Programs** and reinstall with the box ticked.

4. Click **Install Now**, wait, then click **Close**

---

**To verify either method worked:**
- Open CMD (`Windows + R` → type `cmd` → Enter)
- Type `python --version` and press Enter
- You should see `Python 3.x.x`

---

## Updating the Tool (Admin)

Make changes to `reorganise.py` on your machine, then push:

```
git add reorganise.py
git commit -m "describe what changed"
git push
```

The team gets the update automatically next time they open `00.FileOrganizer.bat`.
