import os

def calculate_average(grades):
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0

def create_file():
    if not os.path.exists('resourse'):
        os.makedirs('resourse')
    
    file_path = os.path.join('resourse', 'students.txt')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('Иванов Иван:5,4,3,5\n')
        file.write('Петров Петр:4,3,4,4\n')
        file.write('Сидорова Мария:5,5,5,5\n')

    print(f"Файл {file_path} создан")

def process_students():
    try:
        students = []

        file_path = os.path.join('resourse', 'students.txt')

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                name, grades_str = line.split(':')

                grades = list(map(int, grades_str.split(',')))

                avg_score = calculate_average(grades)
                students.append([name, avg_score])

        result_path = os.path.join('resourse', 'result.txt')

        with open(result_path, 'w', encoding='utf-8') as file:
            file.write("Студенты со средним баллом выше 4,0:\n\n")

            for name, avg_score in students:
                if avg_score > 4.0:
                    file.write(f"{name}: {avg_score:.2f}\n")

        best_student = None
        best_avg = 0
        
        for name, avg in students:
            if avg > best_avg:
                best_avg = avg
                best_student = name
        count = 0

        # хорошие студенты
        for student in students:
            if student[1] > 4.0:
                count = count + 1

        print("РЕЗУЛЬТАТЫ ОБРАБОТКИ СТУДЕНТОВ\n")
        print(f"Всего студентов: {len(students)}")
        print(f"Студентов с баллом > 4.0: {count}")
        print(f"\nЛучший студент: {best_student}")
        print(f"Средний балл: {best_avg:.2f}")
        print(f"\nРезультаты сохранены в {result_path}")

    except FileNotFoundError:
        print("Ошибка! Файл resource/students.txt не найден")    

    except Exception as e:
        print(f"Произошла ошибка: {e}")

process_students()
create_file()