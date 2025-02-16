x, y, z = input('Question? ').split()
x = int(x)
z = int(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print('expression unknown')
    
print(f'{result:.1f}')
