# LAB1-Array — How to run

This folder contains solutions and tests for LAB1 (Array exercises) implemented in Python.

Files added:
- `src/lab1_ex1.py` — 1D array exercises (student stats, Inventory). Demo available in `__main__`.
- `src/lab1_ex2.py` — 2D array exercises (score analysis and simple cinema seating manager). Demo available in `__main__`.
- `tests/test_lab1_ex1.py` — unit tests for lab1_ex1.
- `tests/test_lab1_ex2.py` — unit tests for lab1_ex2.

Requirements
- Python 3.x (the repository already assumes Python 3)

Run tests (PowerShell)

```powershell
# From repository root (c:\Users\asus\Desktop\DSA2025\DSA-2025-Array)
python -m unittest discover -s .\LAB1-Array\tests -p "test_*.py" -v
```

Run a quick demo manually (PowerShell)

```powershell
# Run demo in lab1_ex1
python .\LAB1-Array\src\lab1_ex1.py
# Run demo in lab1_ex2
python .\LAB1-Array\src\lab1_ex2.py
```

Notes
- Tests insert the `src/` directory into `sys.path` so the modules can be imported.
- If you want additional features (more tests, CLI menus, file persistence), tell me and I can add them.

