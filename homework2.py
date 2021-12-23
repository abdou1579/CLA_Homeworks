from os import X_OK


file = open('high.txt')
students_names = file.read()
students_list = students_names.split('\n')
print(students_list)
print(students_list[0:2])
print(students_list[2:-1])
for i in range(len(students_list)):
    if(students_list=="anony x"):
        print("the name is in the list")

for i in "abcdefjhijklmnopqrstuvwxyz":    
    open(i+".txt",'w')        
        