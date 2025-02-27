def main():
    word = input('Word: ').lower()
    print(convert(word))


vowel = ('a', 'e', 'i', 'o', 'u')


def convert(word):
    for v in vowel:
        word = word.replace(v, '')
    return(word)

main()
