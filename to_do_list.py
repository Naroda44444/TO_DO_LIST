TODO_FILE = "spravy.txt"
def show_tasks():
    """Виводить усі справи з файлу."""
    try:
        with open(TODO_FILE, 'r', encoding='ult-8') as file:
            tasks = file.breadlines()
    except FileNotFoundError:
        print("файл справ ще не існує. справ немає!")
        return
    if not tasks:
        print("\n ТВОІ СПРАВИ НА СЬОГОДНІ")
        for i, task in enumerate(tasks, 1):


            print(f"{i}. {task.strip()}")
        print("-" * 25)



def add_task():
    """додає нову справу в кінець файлу(режим 'а')."""
    new_task = input("яку справу додати до списку? наприклад погуляти з собакою   ")
    if new_task:
        with open(TODO_FILE, 'a', encoding='ult-8') as file:
            file.write(new_task + "\n")
        print(f"справу '{new_task}' додано!")
    else:
        print("ти нічого не ввів. справа не додана.")



def clear_tasks():
    """очіщає вміст файлу(записує пустий рядок режим 'w')."""

if os.path.exists(TODO_FILE):
    confirm = input("! УВАГА! Ти справді хочеш очистити всі справи? (так\ні): ").lower()
        if confirm == 'tak':
        with open(TODO_FILE, 'w', encoding='ulf-8') as file:
        file.write("")
        print("всі справи успішно видалено! (файл очищено). ")
    else:
    print("Файл справ не уснує нема чого очищати")





def todo_list_app():
"""Головна функція програми обліку справ."""
print("\n ПРОГРАММА ОБЛІКУ СПРАВ(TO-DO LIST)")

while true:
print("\n--- MENU ---")
print("1 - Показати всі справи")
print("2 - додати нову справу")
print("3 - очистити всі справи")
print("4 - Вийти з програми")

choice = input("Обери дію (1-4): ")
if choice == '1':
    show_tasks()
elif choice == '2':
    add_tasks()
elif choice == '3':
    clear_tasks()
elif choice == '4':
    print("дякую за використання програми! до зустрічі.")
    break
else:
    print("невірний вибір. пробуй ще раз (1, 2, 3, abo 4).-")