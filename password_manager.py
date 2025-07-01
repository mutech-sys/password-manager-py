def view():
    with open('passed.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()    # removes the new line character from the end of the line
            usr, pwd = line.split("|")    # to get username and password sperately
            print(f"USERNAME: {usr}, PASSWORD: {pwd}")

def add():
    username = input("ENTER THE USERNAME: ")
    passwd = input("ENTER THE PASSWORD: ")

    with open("passed.txt", 'a') as f:
        f.write(username + "|" + passwd + "\n")


while True:
    mode = input(r"What do you intend to do? (view, add) Or 'q' to quit : ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("INVALID INPUT: ")
        continue