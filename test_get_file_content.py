from functions.get_file_content import get_file_content
import os

def test_get_file_content():
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print()

    # New test cases
    print("--- main.py ---")
    main_py_content = get_file_content("calculator", "main.py")
    print(main_py_content)
    print()

    print("--- pkg/calculator.py ---")
    calculator_py_content = get_file_content("calculator", "pkg/calculator.py")
    print(calculator_py_content)
    print()

    print("--- /bin/cat (outside permitted directory) ---")
    bin_cat_content = get_file_content("calculator", "/bin/cat")
    print(bin_cat_content)
    print()

    print("--- pkg/does_not_exist.py ---")
    does_not_exist_content = get_file_content("calculator", "pkg/does_not_exist.py")
    print(does_not_exist_content)
    print()

if __name__ == "__main__":
    test_get_file_content()
