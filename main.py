
try:
    with open("text.txt", "w") as file:
        file.write('Engineering fights going melee. Legendary like Tiger JK')

    with open("text.txt", "r") as file:
        for line in file:
            print("Original text: ", line, end=" ")
    print()
    sevenlist = []
    splitted = line.split(' ')
    for item in splitted:
        l = len(item)
        #print(l, end=" ")
        if l > 7:
            sevenlist.append(item)
            with open('seven.txt', 'w') as fle:
                print(f"Words that contain 7 or more letters: {sevenlist}", file=fle)
                print(f"Words that contain 7 or more letters: {item}")


except Exception as ex:
    print(f"Error: {ex}")
