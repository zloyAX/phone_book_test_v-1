import msvcrt

while True:
    if msvcrt.kbhit():  # Проверяем, есть ли нажатие клавиши
        key = msvcrt.getch()  # Считываем символ
        if key == b"\x1b":  # Код клавиши Esc (байтовая строка)
            print("Нажата клавиша Esc")
            break
        else:
            try:
                print(
                    f"Нажата клавиша: {key.decode()}"
                )  # Пытаемся декодировать, если это обычный символ
            except UnicodeDecodeError:
                print(
                    f"Нажата специальная клавиша: {key}"
                )  # Выводим байтовое представление для спец. клавиш
