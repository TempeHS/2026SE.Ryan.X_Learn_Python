def file_name():
    file = input("File type? ")
    if file.endswith('.gif'):
        print('image/gif')
    elif file.endswith('.jpg'):
        print('imge/jpg')
    elif file.endswith('.png'):
        print('image/png')
    elif file.endswith('.png'):
        print('image/png')
    elif file.endswith('.pdf'):
        print('application/pdf')
    elif file.endswith('.txt'):
        print('text/plain')
    elif file.endswith('.zip'):
        print('application/zip')
    else:
        print('file not found')

file_name()