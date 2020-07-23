def master_yoda(text):
    list1 = text.split(" ")
    list2 = []
    string = ""
    counter = len(list1)
    for i in reversed(range(counter)):
        list2.append(list1[i])
        j = " ".join(list2)
    print(j)
