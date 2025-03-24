def main():
    while True:
        try:
            percentage = (input('What is x/y: '))
            result = (convert(percentage))
            if result <= 1:
                print('E')
            elif result >= 99:
                print('F')
            else:
                print(f'{result}%')
            break
        except ValueError:
            print('percent not valid')



def convert(percentage):
    x, y = map(int, percentage.split('/')) 
    if y == 0:
        raise ValueError('Denominator cannot be zero')
    if x > y:
        raise ValueError('Numerator cannot be greater than denominator')
    return int((x / y) * 100)



main()