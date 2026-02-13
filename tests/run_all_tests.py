import subprocess
import os
import sys
sys.path.append(os.path.abspath("."))

test_files = [
    "basic_test.py",
    "function_test.py",
    "exception_test.py",
    "thread_test.py",
    "async_test.py",
    "project_test.py",
    "stress_test.py"
]

for file in test_files:
    print(f"\nRunning {file}...\n")
    result = subprocess.run(
        ["timetrace", f"tests/{file}"],
        input="q\n",
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        print(f"FAILED: {file}")
        print(result.stderr)
    else:
        print(f"PASSED: {file}")
