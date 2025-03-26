Food = {"Baja Taco": 4.25,
	    "Burrito": 7.50,
		"Bowl": 8.50,
		"Nachos": 11.00,
		"Quesadilla": 8.50,
		"Super Burrito": 8.50,
		"Super Quesadilla": 9.50,
		"Taco": 3.00,
		"Tortilla Salad": 8.00
}



def main():
    total = 0
    while True:
        order = menu()
        if order:
            total += Food[order]
            print(f'order is {order}, price is ${Food[order]:.2f}')
            print(f'Total so far: ${total:.2f}')

def menu():
    while True:
        try:
            order = input('Order?: ').strip()
            if order in Food:
                return order
            else:
                print('Item not available')
        except Exception as e:
            print(f'Error occured: {e}')

main()