from functions.get_file_content import get_file_content

# 
def test():
    result = get_file_content("calculator", "lorem.txt")
    trunc_message = "[...File" in result
    print(f"Result length: {len(result)}")
    print(f"Message trunced: {trunc_message}")
    print("")
    # 
    result = get_file_content("calculator","main.py")
    print(result)
    print("")
    #
    result = get_file_content("calculator","pkg/calculator.py")
    print(result)
    print("")
    #
    result = get_file_content("calculator","/bin/cat")
    print("this one should be an error")
    print(result)
    print("")
    #
    result = get_file_content("calculator","pkg/does_not_exist.py")
    print("this one should be an error")
    print(result)
    print("")
    # 

# 
if __name__ == "__main__":
    test()