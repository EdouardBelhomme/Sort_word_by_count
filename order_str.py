def sort_string(list_string):

    list_str_unique = []
    list_return = []
    i = 1
    y = 0

    list_str_unique.append({"word" : list_string[0], "count" : 1})

    while i < len(list_string):
        while y < len(list_str_unique):
            if list_string[i] != list_str_unique[y]["word"]:
                y += 1
                if y >= len(list_str_unique):
                    list_str_unique.append({"word" : list_string[i], "count" : 1})
                    break
            else:
                list_str_unique[y]["count"] += 1
                break
        y = 0
        i += 1
    
    list_str_unique = sorted(list_str_unique, key = lambda str_unique: (-str_unique["count"], str_unique["word"]))
    
    for str_unique in list_str_unique:
        if (str_unique["count"] > 0):
            list_return.append(str_unique["word"] + " " + str(str_unique["count"]))

    print(list_return)
    return(list_return)

sort_string(['les','can', 'can','bin', 'bin','les', 'les'])



""" i = 1
while i < 10:
    print (i)
    print("hello")
    if (i == 8):
        break
    elif (i == 5):
        i=6
        continue
    i += 2
 """