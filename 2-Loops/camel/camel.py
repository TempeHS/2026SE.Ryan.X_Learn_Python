def main():
    Camel = input('Word: ').strip()
    print(camel(Camel))

def camel(Camel):
    for letter in Camel:
        if letter.isupper():
            Camel = Camel.replace(letter,'_' + letter.lower())
    return(Camel)


main()

