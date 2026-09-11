from functions.write_file import write_file

def test_write_file():
    # Test case 1
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Test 1 (lorem.txt): {result1}")

    # Test case 2
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Test 2 (pkg/morelorem.txt): {result2}")

    # Test case 3
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Test 3 (/tmp/temp.txt): {result3}")

if __name__ == "__main__":
    test_write_file()
