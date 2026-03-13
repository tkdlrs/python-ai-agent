from functions.write_file import write_file

# 
def test():
    result = write_file("calculator", "lorem.txt", "Wait, this isn't lorem ipsum")
    print("this should overwrite the file")
    print(result)
    print("")
    # 
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("This should make a new file")
    print(result)
    print("")
    # 
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("This should not be allowed.")
    print(result)
    print("")

# 
if __name__ == "__main__":
    test()
