import json
import os

RESOURCE_DIR = 'resourse'
LIBRARY_FILE = os.path.join(RESOURCE_DIR, 'library.json')

def load_books():
    if not os.path.exists(RESOURCE_DIR):
        os.makedirs(RESOURCE_DIR)
    
    if not os.path.exists(LIBRARY_FILE):
        books = [
            {"id": 1, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "available": True},
            {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "available": True},
        ]
        save_books(books)
        print("Файл создан с начальными данными")
        return books
    
    with open(LIBRARY_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_books(books):
    with open(LIBRARY_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def show_books(books):
    if not books:
        print("Библиотека пуста")
        return
    
    print("\n" + "="*60)
    for book in books:
        status = "Доступна" if book['available'] else "Выдана"
        print(f"ID:{book['id']} | {book['title']} | {book['author']} | {book['year']} | {status}")
    print("="*60)

def search_books(books):
    query = input("Введите название или автора: ").lower()
    found = [b for b in books if query in b['title'].lower() or query in b['author'].lower()]
    
    if found:
        for book in found:
            status = "Доступна" if book['available'] else "Выдана"
            print(f"{book['title']} - {book['author']} ({status})")
    else:
        print("Книги не найдены")

def add_book(books):
    title = input("Название: ")
    author = input("Автор: ")
    year = int(input("Год: "))
    
    new_id = max([b['id'] for b in books], default=0) + 1
    books.append({"id": new_id, "title": title, "author": author, "year": year, "available": True})
    save_books(books)
    print(f"Книга '{title}' добавлена")

def change_status(books):
    try:
        book_id = int(input("Введите ID книги: "))
        for book in books:
            if book['id'] == book_id:
                book['available'] = not book['available']
                save_books(books)
                print(f"Статус изменен на: {'Доступна' if book['available'] else 'Выдана'}")
                return
        print("Книга не найдена")
    except ValueError:
        print("Ошибка ввода")

def delete_book(books):
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        for i, book in enumerate(books):
            if book['id'] == book_id:
                del books[i]
                save_books(books)
                print("Книга удалена")
                return
        print("Книга не найдена")
    except ValueError:
        print("Ошибка ввода")

def export_available(books):
    available = [b for b in books if b['available']]
    if not available:
        print("Нет доступных книг")
        return
    
    file_path = os.path.join(RESOURCE_DIR, 'available_books.txt')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("Доступные книги:\n")
        f.write("-"*30 + "\n")
        for book in available:
            f.write(f"{book['title']} - {book['author']} ({book['year']})\n")
    print(f"Экспортировано {len(available)} книг в {file_path}")

def main():
    books = load_books()
    
    while True:
        print("\n1. Все книги")
        print("2. Поиск")
        print("3. Добавить")
        print("4. Изменить статус")
        print("5. Удалить")
        print("6. Экспорт")
        print("7. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            show_books(books)
        elif choice == '2':
            search_books(books)
        elif choice == '3':
            add_book(books)
            books = load_books()
        elif choice == '4':
            change_status(books)
            books = load_books()
        elif choice == '5':
            delete_book(books)
            books = load_books()
        elif choice == '6':
            export_available(books)
        elif choice == '7':
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()