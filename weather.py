dic = {}
i = 0
while True:
    day = input("enter the day of the week : ")
    temp = int(input ("enter temp of " + day + " : "))
    dic[day] = temp
    i = i + 1
    if(i > 7):
        break
    
    total = sum(dic.values())
    # avg = sum/7
    print(dic)
    print(total)
    # print(sum/7)
