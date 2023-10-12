total =int(input("enter total numbers"))
numbers=[]
for i in range(total):
    numbers.append(int(input(f'enter {i+1} value ')))
print(numbers)
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print (f"no of even no are {even} \nno of odd  no are {odd} ")