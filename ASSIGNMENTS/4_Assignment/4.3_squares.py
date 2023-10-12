def square(x):
    return x ** 2
numbers = []
max=int(input('enter the number of items in list'))
for i in range(max):
    num=int(input(f'enter {i+1} value '))
    numbers.append(num)
squared_numbers = list(map(square, numbers))
print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)