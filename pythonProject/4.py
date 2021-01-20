"""
Задача 4. Реализирайте конзолно приложение за интерактивно въвеждане и редактиране на таблицата от задача 3. 
Приложението следва да поддържа текстово меню с възможности за:
1) прочитане на таблицата от текстов файл;
2) запис на таблицата в текстов файл;
3) редактиране на таблицата;
4) създаване на нова празна таблица с възможност за редактиране;
5) изход от програмата.
Редактирането на таблицата трябва да стане в текстов вид, интерактивно от клавиатурата с поддържане на 
активен курсор (символ '#') и с натискане на '+' за запълване на клетката където е курсора и '-' за изчистване на клетката, 
където е курсора. Преместването на курсора става със стрелките от клавиатурата.
След натискане на всеки клавиш се извежда цялата таблица и един празен ред за разделител. Редактирането приключва с 
натискане на клавиша <Enter>, след което се връщаме в главното меню на програмата, като редактираната таблица се запомня.
"""

table = None

def print_menu():
    print('Меню:\n\
    1 прочитане на таблицата от текстов файл\n\
    2 запис на таблицата в текстов файл\n\
    3 редактиране на таблицата\n\
    4 създаване на нова празна таблица с възможност за редактиране\n\
    5 изход от програмата')

def read_from_file():
    global table
    print("Въведете име на файл: ", end='')
    filename = input().strip()

    try:
        with open(filename) as f:
            read_data = f.readlines()
            table = list(map(lambda x: list(x.strip()), read_data))
    except:
        print("Грешка при четенето на файла...")

def write_to_file():
    global table
    if table is None:
        print("Няма заредена таблица")
        return

    print("Въведете име на файл: ", end='')
    filename = input().strip()

    try:
        with open(filename, "w") as f:
            for row in table:
                f.write(''.join(row))
                f.write('\n')
    except:
        print("Грешка при записването на файла...")

def create_empty_table():
    global table
    print("Въведете размери РЕДОВЕ КОЛОНИ")
    try:
        user_input = list(map(lambda x: int(x), input().strip().split(' ')))
        if len(user_input) != 2:
            print("Неправилно въведени размери...")
            return
    except:
        print("Неправилно въведени размери...")
        return
    
    rows = user_input[0]
    cols = user_input[1]

    table = [['0'] * cols for _ in range(rows)]
    print("Успешно създадена нова таблица")

def print_table_with_cursor(table, cursor):
    for row in range(len(table)):
        for col in range(len(table[row])):
            if row != cursor[0] or col != cursor[1]:
                print(table[row][col], end='')
            else:
                print('#', end='')
        print()
    print()

# I don't use the arrow keys because to do so I need external libraries
def edit_current_table():
    global table
    if table is None:
        print("Няма заредена таблица")
        return

    cursor = [0, 0]

    key_pressed = None
    while key_pressed != 'Enter':
        print_table_with_cursor(table, cursor)
        print("AWSD to move, ENTER to exit, + and - to change the state of the current cell")
        key_pressed = input().strip().lower()
        if key_pressed == 'w':
            cursor[0] = max(0, cursor[0] - 1)
        elif key_pressed == 's':
            cursor[0] = min(len(table) - 1, cursor[0] + 1)
        elif key_pressed == 'd':
            cursor[1] = min(len(table) - 1, cursor[1] + 1)
        elif key_pressed == 'a':
            cursor[1] = max(0, cursor[1] - 1)
        elif key_pressed == '+':
            table[cursor[0]][cursor[1]] = '*'
        elif key_pressed == '-':
            table[cursor[0]][cursor[1]] = '0'
        else:
            key_pressed = 'Enter'

if __name__ == '__main__':
    menu_choice = 0
    while menu_choice != 5:
        print_menu()
        menu_choice = int(input())
        if menu_choice == 1:
            read_from_file()
        elif menu_choice == 2:
            write_to_file()
        elif menu_choice == 3:
            edit_current_table()
        elif menu_choice == 4:
            create_empty_table()
