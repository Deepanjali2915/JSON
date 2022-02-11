# i=1
# while i<=100:
#     print(i)
#     i=i+1

# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
# print(sum)    



lst=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

    result = list((lst[i:i+n] for i in range(0, len(lst), n)))