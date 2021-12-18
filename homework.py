x=list(range(1, 299))
y=0
while(y< len(x)):
    if(x[y]%2 != 0):
        del x[y]
        y +=1
print(x)
print(len(x))
squared_list=[number ** 2 for number in x]
print(squared_list)
for i in x:
    if(i == 57) :
        print ("Element Exists")
