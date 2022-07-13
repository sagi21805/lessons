def write_in_line(lineNum:int, content:str, fileName:str):
    """the function writes in a specific line

    Args:
        lineNum (int): the line you want to write in
        content (str): what you writujme in the line           
        fileName (str): the file you want to write into.
    """
    file = open(fileName, "r")
    fileContent:list = file.readlines()
    if len(fileContent) < lineNum: 
        for i in range(len(fileContent), lineNum):
            fileContent.append("\n")
    file.close()
    fileContent[lineNum - 1] = content
    file = open(fileName, "w")
    file.writelines(fileContent)
    file.close()


def read_line(lineNum:int, fileName:str) -> str:
    file = open(fileName, "r")
    fileContent = file.read().split("\n")
    if len(fileContent) < lineNum:
        print("this line does not exist")
    return fileContent[lineNum - 1]

write_in_line(int(input("enter line number\n")), input("enter content\n"), "newfile.txt")
print(read_line(int(input("enter line number\n")), "newfile.txt"))