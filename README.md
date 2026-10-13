# Shopping List Manager

This repository contains the files for the Week 7 Python assignment.

- `list_warmup.py` demonstrates list indexing, appending, removing, and counting items.
- `shopping_list.py` creates an interactive shopping list manager with add, remove, show, and done commands.
- `list_report.py` prints numbered items and calculates counts and longest item names.

It is safer to check `in` before calling `.remove()` because the list may not contain the item, and removing a missing value would raise an error and crash the program. A membership check lets the program handle the case gracefully and keep running.
