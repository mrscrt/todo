import os

def show_tasks(tasks):
    print("Список задач:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. [{task['status']}] {task['description']}")

def add_task(tasks, description):
    task = {'description': description, 'status': 'Невыполнено'}
    tasks.append(task)
    print(f"Задача '{description}' добавлена в ToDo-лист.")

def complete_task(tasks, task_idx):
    if 1 <= task_idx <= len(tasks):
        tasks[task_idx - 1]['status'] = 'Выполнено'
        print(f"Задача '{tasks[task_idx - 1]['description']}' отмечена как выполненная.")
    else:
        print("Недопустимый номер задачи.")

def main():
    tasks = []
    while True:
        print("\n===== ToDo-лист =====")
        print("1. Просмотреть список задач")
        print("2. Добавить новую задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Выход")

        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            description = input("Введите описание задачи: ")
            add_task(tasks, description)
        elif choice == '3':
            task_idx = int(input("Введите номер задачи, которую хотите отметить как выполненную: "))
            complete_task(tasks, task_idx)
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Недопустимый выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
