from functions.run_python_file import run_python_file

def test_run_python_file():
    print("--- Case 1: run_python_file('calculator', 'main.py') ---")
    res1 = run_python_file("calculator", "main.py")
    print(res1)
    print()

    print("--- Case 2: run_python_file('calculator', 'main.py', ['3 + 5']) ---")
    res2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(res2)
    print()

    print("--- Case 3: run_python_file('calculator', 'tests.py') ---")
    res3 = run_python_file("calculator", "tests.py")
    print(res3)
    print()

    print("--- Case 4: run_python_file('calculator', '../main.py') ---")
    res4 = run_python_file("calculator", "../main.py")
    print(res4)
    print()

    print("--- Case 5: run_python_file('calculator', 'nonexistent.py') ---")
    res5 = run_python_file("calculator", "nonexistent.py")
    print(res5)
    print()

    print("--- Case 6: run_python_file('calculator', 'lorem.txt') ---")
    res6 = run_python_file("calculator", "lorem.txt")
    print(res6)
    print()

if __name__ == "__main__":
    test_run_python_file()
