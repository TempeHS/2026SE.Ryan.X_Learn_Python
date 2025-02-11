deep = input('answer to the Great Question of Life, the Universe and Everything? ')

match deep:
    case '42' | 'Forty two' | 'Forty-two':
        print('Yes')
    case _:
        print('No')