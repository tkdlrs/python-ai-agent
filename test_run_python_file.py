from functions.run_python_file import run_python_file

# 
def test():
    result = run_python_file("calculator", "main.py")
    print("Test 1: Should print the calculator's usage instructions")
    print(result)
    print(" ------------ ")
    # 
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Test 2: Should run the calculator... Which gives a nasty rendered result")
    print(result)
    print(" ------------ ")
    #  
    result = run_python_file("calculator", "tests.py")
    print("Test 3: Should run the calculator's tests successfully")
    print(result)
    print(" ------------ ")
    #  
    result = run_python_file("calculator", "../main.py")
    print("Test 4: This should return an error")
    print(result)
    print(" ------------ ")
    #  
    result = run_python_file("calculator", "nonexistent.py")
    print("Test 5: This should return an error")
    print(result)
    print(" ------------ ")
    #  
    result = run_python_file("calculator", "lorem.txt")
    print("Test 6: This should return an error")
    print(result)
    print(" ------------ ")
    #

# 
if __name__ == "__main__":
    test()

# 
