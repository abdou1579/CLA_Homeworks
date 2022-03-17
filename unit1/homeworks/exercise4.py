try:
    a = 12
    s = "hello"
    print(a+s)
except TypeError:
    print("the two inputs aren't of the same type")
finally :
    print("Finished")
