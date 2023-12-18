import func
while True:
    text = input('Введите текст: ')
    if len(text.split()) > 0:
        clean_text = func.remove_whitespace(text)
        print(clean_text)
        break
    else:
        print('Введите корректный текст!')


