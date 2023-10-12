def triple_number(x):
    return 3 * x
numbers = []
max=int(input('enter the number of items in list'))
for i in range(max):
    num=int(input(f'enter {i+1} value '))
    numbers.append(num)
tripled_numbers = list(map(triple_number, numbers))
print("Original Numbers:", numbers)
print("Tripled Numbers:", tripled_numbers)