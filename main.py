print("Project Ongoing")

def addtask(task):
    afile = open('TaskList.txt', 'a')
    afile.write(task)
    print('Your task has successfully been added!')
    afile.close()

def retrvtask():
    rfile = open('TaskList.txt', 'r')
    ThisLine = rfile.read()
    print('Last Added Task: ')
    print(ThisLine)