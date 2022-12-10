try:
    with open("original.txt", "w") as orgfile:
        print("I wanna be a human", file=orgfile)
        print("'Fore I do some art", file=orgfile)
        print("It's a cruel world", file=orgfile)
        print("But there's gon' be my part", file=orgfile)
        print("'Cause true beauty is a true sadness", file=orgfile)
        print("Now you could feel my madness", file=orgfile)

    with open("original.txt", "r") as fileread:
        v = fileread.readlines()


    with open("copy.txt", "w") as copyfile:
        for item in v:
            print(item.replace("\n", ""), file=copyfile)

    print("Text copied successfully")
except Exception as ex:
    print(f"Error: {ex}")
