



class Main:

    while True:

        print("""
        === Story Generator ===
    1. Создать случайную историю
    2. Создать историю с заданными элементами
    3. Добавить новый элемент в базу данных
    4. Показать список элементов
    5. Выйти""")

        val = input("\nВыберите действие: ")

        match val:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("\nВы вышли за предел диапазона [1 - 5]. Повторите попытку")
