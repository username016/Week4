for num in range(10,20): #The upper bound is excluded (it will not print the number 20)
    print(num)
    
for num in range(20,10,-1): #The upper bound is excluded (it will not print the number 20) and it would decrement from the third value in this case -1 
    print(num)
    
for num in range(10):
    print(num)
    
print("=" * 50)
    
number = [1,12,45,90]
print(type(number))
print((number[0]))
print((number[1]))
print((number[2]))
print((number[3]))


#rather than doing that above do this instead

for index in range(len(number)):
    print(number[index])
    

print((number[-1]))

print(len(number))

for number in number: # the loop varauble number assumes all the values in the iist one by one 
    print(number)

print("=" * 50)

numero = "10232as"[:2]
print(numero)

numb = "10232as"[2:]
print(numb)

print("=" * 50)

# This is iterating over lists and slicing 

numbering = [1,12,45,90]

for index in range (len(numbering)-1,-1,-1): 
   print(numbering[index])

nu = [1,12,45,90]

for nu1m in nu[::-1]:
    print(nu1m)
 
    
print("-" * 50)



    
