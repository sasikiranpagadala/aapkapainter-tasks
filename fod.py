li = eval(input())
l2 =[]
for element in li:
    if element in l2:
        print(element)
        break
    else:
        l2.append(element)