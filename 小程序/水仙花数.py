

"""3-7位数的水仙花数"""

for n in range(3,8):
    list1 = []

    for i in range(10**(n-1),10**n):
        str1 = str(i)
        sum1 = 0
        for j in str1:
            num = int(j)
            sum1 += num**n
        if i == sum1:
              list1.append(i)
    print("%d位数水仙花数,共%d个：%s" % (n, len(list1), list1))