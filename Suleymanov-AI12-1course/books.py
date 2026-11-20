books = [
    "Алхимик"
    "Повелитель мух"
    "Тихий дон"
    "Ведикий Гэтсби"
]

def show_menu():
    print("/n== ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===")
    print("1 - Добавить книгу")
    print("2 - Показать все книги")
    print("3 - Показать последние 5 прочитанных книг")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("7 - Выход")
    
def add_boks():
    name = input("Введите название книги: ")
    books.append(name)
    print("Книга была добавлена!")
def show_books():
    
    for book in books:
        print("Книга найдена!")
        print(book)
    else:
        print("Книга не найдена!")
def find_book():
    if len(books) == 0:
        print("Не найдена!")
    else:
        found = False
        
        for i in range(len(books)):
            if n in books[i].lower():
                print(f"{i + 1}. {books}[i]}")
                found True
        if not found:
            print("Не найдено")
                
                
                
                
while True:
                
                
 number = int(input())
if number == 1:
    show_menu()
if number == 2:
    add_books()
if number == 3:
    show_books()
if number == 0:
    break