l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    l.append(e)
print("Positive numbers in",l,"are: ")
for i in l:
    if i >= 0:
       print(i, end = " ")
