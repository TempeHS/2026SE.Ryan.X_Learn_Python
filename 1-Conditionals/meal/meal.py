def main():
    meal = input('Meal time? ')
    time = convert(meal)

    if 7.0 <= time <= 8.0:
        print('Breakfast time')
    if 12.0 <= time <= 13.0:
        print('Lunch time')
    if 18.0 <= time <= 19.0:
        print('Dinner time')

def convert(meal):
    h, m =(meal.split(':'))
    h = int(h)
    m = int(m)
    return (h + m / 60)

if __name__ == '__main__':
    main()