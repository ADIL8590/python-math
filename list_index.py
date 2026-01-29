def print_list(list, indx=0):
    if (indx==len(list)):
        return
    print(list[indx])
    print_list(list, indx+1)


fruits =["apple", "banana", "nut", "almond"]
print_list(list(fruits))