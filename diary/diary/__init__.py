import sys

from diary import storage

get_connection = lambda: storage.connect('diary.sqlite')



def action_add_task():
    """ Добавить задачу """
    task = input('\nВведите задачу: ')
    content = input('\nВведите описание задачи: ')
    deadline = input('\nУкажите дедлайн: ')

    with get_connection() as conn:
        pk = storage.add_task(conn, task_name, content, deadline)


def action_edit_task():
    """ Отредактировать задачу """
    pk = input('\nВведите id задачи: ')

    with get_connection() as conn:
        task = storage.edit_task_by_pk(conn, pk)

        if task:
            template = '{task[id]} - {task[title_task]} - {task[content} - {task[status]} - {task[deadline]}'
            print(template.format(task=task))
        else:
            print('Задача c {} id не найдена'.format(pk))
            
            title_task = input('\nВведите новое название задачи: ')
            content = input('\nВведите новое описание задачи: ')
            deadline = input('\nВведите новый срок выполнения задачи: ')
            storage.edit_task(conn, title_task, content, deadline, pk)



def action_display_tasks():
     """ Вывести список всех задач """
    with get_connection() as conn:
        tasks = storage.find_all(conn)

    for task in tasks:
        template = '{task[id]} - {task[title_task]} - {task[status]} - {task[deadline]}'
        print(template.format(task=task))


def action_complite_task():
    pk = input('\nВведите id задачи: ')
    with get_connection() as conn:
        storage.complite_task(conn, pk)
        

def action_restart_task():
    pk = int(input('\nВведите id задачи: '))
    with get_connection() as conn:
        storage.restart_task(conn, pk)


def action_delete_task():
    pk = int(input('\nВведите id задачи: '))
    with get_connection() as conn:
        storage.delete_task(conn, pk)


def action_show_menu():
    """Показать меню"""
    print('''
1. Вывести все задачи
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу с начала
6. Удалить задачу
m. Показать меню
q. Выход
''')

def action_exit():
    """Выход"""
    sys.exit(0)


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    actions = {
        '1': action_display_tasks,
        '2': action_add_task,
        '3': action_edit_task,
        '4': action_complite_task,
        '5': action_restart_task,
        '6': action_delete_task,
        'm': action_show_menu,
        'q': action_exit,
    }

    action_show_menu()

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')
