name = input('What is your name? ')


def player_choice():
    choice = input('Rock, Paper or Scissors? ')
    print(f'{name} chose {choice}')

def random_choice():
    return range('Rock', 'Paper', 'Scissor')


player_choice()
