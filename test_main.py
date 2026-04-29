"""
Local test runner for main.py
Run: python test_main.py
"""
import subprocess
import sys

TESTS = [
    {
        "name": "Sample from challenge",
        "input": "2\n4\n3 -1 1 10\n5\n9 -5 -5 -10 10\n",
        "expected": "1\n11250"
    },
    {
        "name": "All positive numbers (should be 0)",
        "input": "1\n3\n1 2 3\n",
        "expected": "0"
    },
    {
        "name": "All negative numbers",
        "input": "1\n3\n-1 -2 -3\n",
        "expected": "98"   # 1 + 16 + 81 = 98
    },
    {
        "name": "Mismatch count → -1",
        "input": "1\n4\n1 2 3\n",
        "expected": "-1"
    },
    {
        "name": "Zero is not positive → included",
        "input": "1\n1\n0\n",
        "expected": "0"   # 0^4 = 0
    },
    {
        "name": "Single negative",
        "input": "1\n1\n-10\n",
        "expected": "10000"  # (-10)^4 = 10000
    },
]

passed = 0
failed = 0

print("=" * 50)
print("Running tests for main.py")
print("=" * 50)

for test in TESTS:
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=test["input"],
        capture_output=True,
        text=True
    )
    actual = result.stdout.strip()
    ok = actual == test["expected"]
    status = "✓ PASS" if ok else "✗ FAIL"
    print(f"{status}  |  {test['name']}")
    if not ok:
        print(f"         Expected : {repr(test['expected'])}")
        print(f"         Got      : {repr(actual)}")
        failed += 1
    else:
        passed += 1

print("=" * 50)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 50)