import os

def create_text_file():
    lines = [
        "Вещи, которыми ты владеешь, в конце концов начинают владеть тобой.",
        "Лишь утратив всё до конца, мы обретаем свободу.",
        "Не разбив яиц, омлет не приготовишь.",
        "Сначала ты должен познать страх, прежде чем сможешь забыть о нём.",
        "Человек, который может контролировать себя, может контролировать мир."
    ]
    if not os.path.exists('resource'):
        os.makedirs('resource')
        print("Папка 'resource' создана!")

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')
    print(f"Файл {file_path} создан")

    file_path = os.path.join('resource', 'text.txt')
    

def analyze_text_file():
    try:
        file_path = os.path.join('resource', 'text.txt')

        # cчитаем файл
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # cчитаем строки
        line_count = len(lines)

        # cчитаем слова
        words = 0
        for line in lines:
            words += len(line.split())

        # cамая длинная строка
        longest = max(lines, key=len)

        print("\n" + "="*50)
        print("РЕЗУЛЬТАТЫ АНАЛИЗА ФАЙЛА text.txt")
        print("="*50)
        print(f"1. Количество строк в файле: {line_count}")
        print(f"2. Количество слов в файле: {words}")
        print(f"3. Самая длинная строка: {longest}")

    except FileNotFoundError:
        print("Ошибка! Файл resource/text.txt не найден")    

create_text_file()
analyze_text_file()