# Main Makefile for project

target:
	python3 src/main.py

test:
	python3 -m py_compile src/main.py src/task.py

check:
	ty check
