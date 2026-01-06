# Lab2 Linked-List — How to run

This folder contains implementations and demos for Linked List exercises.

Files of interest:
- `src/linkedlist.py` — LinkedList, DoublyLinkedList, StudentLinkedList implementations
- `src/run_lab2.py` — Demo runner that executes exercise1, exercise2, student manager demo, and doubly linked-list demo
- `tests/test_linkedlist.py` — unit tests for the implementations

Run tests (PowerShell)

```powershell
# From repository root
python -m unittest discover -s .\"Lab2 Linked-List\"\tests -p "test_*.py" -v
```

Run demo (PowerShell)

```powershell
# From repository root
python .\"Lab2 Linked-List\"\src\run_lab2.py
```

If you want additional features (interactive CLI, CSV import/export for students, more operations), tell me and I can add them.
