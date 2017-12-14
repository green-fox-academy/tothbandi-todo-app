def print_usage():
    print('''Command Line Todo application
=============================

Command line arguments:
 -l   Lists all the tasks
 -a   Adds a new task
 -r   Removes an task
 -c   Completes an task''')

def print_todo_list():
    file_name = 'todo_list.txt'
    try:
        my_file = open(file_name, 'r')
        lines = my_file.readlines()
        for i in range(len(lines)):
            print('{} - {}'.format(i, lines[i]), end='')
        print()
        my_file.close()
    except IOError:
        print("cannot open", file_name)