
try:
    with open("4stfile.txt", "w") as file4:
        print("whats", file= file4)
        print("absu", file= file4)
        print("absu", file= file4)
        print("mullayo", file= file4)

    with open("4stfile.txt", "r") as file4:
        con = file4.readlines()

    lst = []
    with open("5ndfile.txt", "w") as file5:
        for item in con:
            repl = lst.append(item.replace("\n", ""))

            #print(repl[::-1])
            #print(f"{reversed(repl)}", file=file5)
            re = lst[::-1]

            repl = lst[-1]
            l = []
            for i in repl:
                l.append(i)

            l = l.reverse()
            print(l)


            del lst[0]
            #print(i)
            #print(re, "\n")
            #print(f"{lst[:-1]}", file=file5)

    print("--DONE--")
except Exception as ex:
    print(f"Error: {ex}")
