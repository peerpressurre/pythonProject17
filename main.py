try:
    with open("1file.txt", "w") as file:
        print("bad bye", file=file)
        print("seoul", file=file)
        print("moonchild", file=file)
        print("everything goes", file=file)

    with open("1file.txt", "r") as file1:
        reader = file1.readline()
        count = reader.count(' ')
        reader1 = file1.readline()
        count1 = reader1.count(' ')
        reader2 = file1.readline()
        count2 = reader2.count(' ')
        reader3 = file1.readline()
        count3 = reader3.count(' ')

        if count == 0:
            with open("2file.txt", "w") as file:
                print(reader, file=file)
                print("------------", file=file)
                print(reader1, file=file)
                print(reader2, file=file)
                print(reader3, file=file)

        if count1 == 0:
            with open("2file.txt", "w") as file:
                print(reader, file=file)
                print(reader1, file=file)
                print("------------", file=file)
                print(reader2, file=file)
                print(reader3, file=file)

        if count2 == 0:
            with open("2file.txt", "w") as file:
                print(reader, file=file)
                print(reader1, file=file)
                print(reader2, file=file)
                print("------------", file=file)
                print(reader3, file=file)

        if count3 == 0:
            with open("2file.txt", "w") as file:
                print(reader, file=file)
                print(reader1, file=file)
                print(reader2, file=file)
                print(reader3, file=file)
                print("------------", file=file)
        # print(reader)
        # print(f"{count}")
except Exception as ex:
    print(f"Error:{ex}")