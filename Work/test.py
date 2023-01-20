def mygenerator():
     yield 1
     yield 2
     yield 3

g=mygenerator()

value=next(g)
print(value)

value=next(g)
print(value)

value=next(g)
print(value)

value=next(g)
print(value)

# Below is the second code of the generator if you want to run than comment the above code and uncomment the code below

#mygenerator=(i for i in range(10) if i % 2==0)
#for i in mygenerator:
     #print(i)
