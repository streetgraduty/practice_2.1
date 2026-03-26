import datetime
import os

def format_number(num):
    if num == int(num):
        return str(int(num))
    return str(num)

def calculator(first_number, second_number, action):
    if action == "+":
        return first_number + second_number
    elif action == "-":
        return first_number - second_number
    elif action == "*":
        return first_number * second_number
    elif action == "/":
        if second_number == 0:
            return "Ошибка, деление на ноль"
        return first_number / second_number
    else:
        return "Ошибка, неизвестная операция"
    
def create_file():
    if not os.path.exists('resourse'):
        os.makedirs('resourse')

    file_path = os.path.join('resourse', 'calculator.log')

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("")
        print("Файл calculator.log создан успешно!")
    else:
        print("Файл calculator.log уже существует!")

def show_last_operation():
    file_path = os.path.join('resourse', 'calculator.log')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            if len(lines) >= 5:
                last_lines = lines[-5:]
            else:
                last_lines = lines
        
            print("Последние 5 операций:\n")
            for line in last_lines:
                print(line.strip())
            print('\n')

    except FileNotFoundError:
        print("Ошибка! Лог-файл пока пуст")

def clearing_logs(first_number, second_number, action, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = os.path.join('resourse', 'calculator.log')

    #форматируем для корректног вывода
    first_num_str = format_number(first_number)
    second_num_str = format_number(second_number)

    if isinstance(result, (int, float)):
        result_str = format_number(result)
    else:
        result_str = result

    log_entry = f"[{timestamp}] {first_num_str} {action} {second_num_str} = {result_str}\n"
    
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(log_entry)



def main():
    create_file()
    show_last_operation()

    while True:
        try:
            print("Выберите действие:")
            print("1. Калькулятор")
            print("2. Выход")
            choice = input()
            

            if choice == "1":
                first_number = input("Введите первое число: ")
                second_number = input("Введите второе число: ")
                action = input("Введите нужную операцию (+, -, *, /): ")

                first_num = float(first_number)
                second_num = float(second_number)

                result = calculator(first_num, second_num, action)
                
                first_num_str = format_number(first_num)
                second_num_str = format_number(second_num)

                if isinstance(result, (int, float)):
                    result_str = format_number(result)
                    clearing_logs(first_num, second_num, action, result)
                else:
                    result_str = result
                print(f"\nРезультат: {first_num_str} {action} {second_num_str} = {result_str}")
                
            elif choice == "2":
                break
            else:
                print("Некоректный выбор действия")

        except ValueError:
            print("Ошибка, введите корректные числа!")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()