FILEPATH = "todos.txt"


def get_todo(filepath=FILEPATH):
    """Read text file and return alist of to-do items"""
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_args)


if __name__ != '__main__':
    # print('Hello')
    print(get_todo())
