import os

def create_products_file():
    file_path = os.path.join('resourse', 'products.csv')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Название,Цена,Количество\n")
        file.write("Яблоки,100,50\n")
        file.write("Бананы,80,30\n")
        file.write("Молоко,120,20\n")
        file.write("Хлеб,40,100\n")
    print("Файл products.csv создан успешно!")

def load_products():
    products = []
    try:
        file_path = os.path.join('resourse', 'products.csv')

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i in range(1, len(lines)):
                if lines[i].strip():
                    name, price, quantity = lines[i].strip().split(',')
                    products.append({
                        'name': name,
                        'price': int(price),
                        'quantity': int(quantity)
                    })
    except FileNotFoundError:
        print("Файл не найден, создайте его сначала")
    return products

def save_products(products):
    file_path = os.path.join('resourse', 'products.csv')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Название,Цена,Количество\n")
        for product in products:
            file.write(f"{product['name']},{product['price']},{product['quantity']}\n")
    print("Данные сохранены!")

def add_product(products):
    name = input("Введите название товара: ")
    price = int(input("Введите цену: "))
    quantity = int(input("Введите количество: "))
    
    products.append({
        'name': name,
        'price': price,
        'quantity': quantity
    })
    print(f"Товар '{name}' добавлен!")

def search_product(products):
    search_name = input("Введите название товара для поиска: ")
    found = False
    
    for product in products:
        if product['name'].lower() == search_name.lower():
            print(f"\nНайден товар:")
            print(f"Название: {product['name']}")
            print(f"Цена: {product['price']}")
            print(f"Количество: {product['quantity']}")
            found = True
            break
    
    if not found:
        print("Товар не найден!")

def calculate_total_cost(products):
    total = 0
    for product in products:
        total += product['price'] * product['quantity']
    
    print(f"Общая стоимость всех товаров: {total} руб.\n")

def show_menu():
    print("УПРАВЛЕНИЕ ТОВАРАМИ\n")
    print("1. Добавить новый товар")
    print("2. Поиск товара по названию")
    print("3. Расчет общей стоимости")
    print("4. Выйти и сохранить\n")


# Выполнение задачи 3
create_products_file()
products = load_products()

while True:
    show_menu()
    choice = input("Выберите действие (1-5): ")
    
    if choice == '1':
        add_product(products)
    elif choice == '2':
        search_product(products)
    elif choice == '3':
        calculate_total_cost(products)
    elif choice == '4':
        save_products(products)
        print("Программа завершена!")
        break
    else:
        print("Неверный выбор! Попробуйте снова.")