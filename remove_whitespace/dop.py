def remove_extra_newlines(text):
    lines = text.split('\n')
    cleaned_lines = []

    for line in lines:
        if line.strip():  # Проверяем, что строка не пустая после удаления пробелов
            cleaned_lines.append(line.strip())

    clean_text = '\n'.join(cleaned_lines)
    return clean_text

while True:
    text = input('Введите текст: ')
    if len(text.split()) > 0:
        clean_text = remove_extra_newlines(text)
        print(clean_text)
        break
    else:
        print('Введите корректный текст!')