

amount_due = 50


def Coins():
    global amount_due
    while amount_due > 0:
        coin = int(input(f'amount_due: {amount_due}, coin: '))
        if coin == 5 or 10 or 25:
            amount_due -= coin
            print(f'amount_due: {amount_due}')
            
        else:
            print(f'invalid coin, {amount_due} remaining')
            

Coins()
    

    

