Purpose
-------
This repository is a small Windows GUI automation script using Python and `pyautogui` (single file: `arquivo.py`). The guidance below helps an AI agent be productive by describing the project's shape, conventions, and safe developer workflows.

Quick File Reference
- `arquivo.py`: main automation functions. Example: `abrir_navegador()` calls `pyautogui.press('win')`, `pyautogui.write('chrome')`, `pyautogui.press('enter')` and uses `sleep(3)` for timing.

Big picture
- Single-process, desktop GUI automation targeted at Windows (script launches Chrome via the Windows key + typing). There is no server, package structure, or CI configuration in the repo.
- The script manipulates the active desktop session — timing, focus, and screen resolution matter. Treat it as an interactive automation task, not a headless service.

Key patterns and conventions (from the code)
- Uses `pyautogui` for keyboard/GUI actions and `time.sleep` for waits. Expect functions to sequence `press`/`write`/`enter` with explicit sleeps.
- Comments and identifiers are in Portuguese (e.g., `abrir_navegador`). Keep new identifiers and comments consistent with Portuguese naming.
- No image recognition or coordinate-based clicks are present yet — avoid adding brittle absolute-coordinates without documenting resolution assumptions.

Developer workflows
- Install dependencies in a venv and run on Windows. Minimal commands:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pyautogui
```

- Run the script interactively (do not run on a machine you need to use while it executes):

```powershell
python arquivo.py
```

- Debugging tips:
  - Add short `print()` statements between `pyautogui` actions to log progress.
  - Use small incremental sleeps while testing (e.g., `sleep(0.5)`) and increase where needed.
  - Use a disposable VM or dedicated test desktop to validate flows.

Safety and reliability notes
- `pyautogui` controls the mouse/keyboard — keep `pyautogui.FAILSAFE = True` (move mouse to top-left to abort). Do not remove the failsafe.
- Prefer screen-based waits (e.g., `pyautogui.locateOnScreen`) over fixed sleeps where possible; when adding such waits, include fallback timeouts.
- Document any assumptions about display scale or resolution when adding coordinate clicks.

Integration points & external dependencies
- External dependency: `pyautogui` (and its transitive requirements like `Pillow`). No network or cloud integrations are present.
- The script launches Chrome by typing `chrome` after pressing the Windows key — this assumes Chrome is in the Windows search path and the OS language/keyboard layout behaves as expected.

What an AI agent should do first
- Keep changes minimal and explicit: add functions next to existing ones, mirror Portuguese naming, and preserve `sleep`-based sequencing unless replacing with image-based waits.
- When adding features that click or type, include resolution notes and enable failsafe handling.
- Provide runnable examples and short tests that can be manually verified on a Windows VM.

If anything in this file is unclear or you'd like more details (e.g., preferred virtualenv tools, additional examples, or a simple test harness), tell me which section to expand.
