file=open(".\student_names.txt","r")

#1 Reading the file
students=file.read()

#2 Writing a list of random names
file=open(".\student_names.txt","w")
file.write(students + '\nMohammed Ali\nBruce Wayne\nSimon Minter')

#3 Reading the n first lines
i=0
n=int(input("Chose the number of lines :"))
file=open(".\student_names.txt","r")
print("The 5 first lines are :")
for line in file:
    if i==n :
        break
    else :
        print(line)
        i+=1

#4 Reading the n last lines
file=open(".\student_names.txt","r")
j=0
lines=file.readlines() #to get the number of lines
file=open(".\student_names.txt","r")
print("The 5 laste lines are :")
for line in file:
    j+=1
    if j>len(lines)-n :
         print(line)

#5)Cheking if x is in the file
file=open(".\student_names.txt","r")
x="jake flame"
print("Is",x,"in the file? ", x in file)

#6)Generating the files
for t in "abcdefghijklmnopqrstuvwxyz":
    open(t+".txt",'w+')
