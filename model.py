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
        if len(lines) == 0:
            print('No todos for today! :)')
        else:
            for i in range(len(lines)):
                print('{} - {}'.format(i + 1, lines[i]), end='')
            print()
        my_file.close()
    except IOError:
        print("cannot open", file_name)

def add_todo(task):
    file_name = 'todo_list.txt'
    try:
        my_file = open(file_name, 'a')
        my_file.write('\n[ ] ' + task )
        my_file.close()
    except IOError:
        print("cannot open", file_name)

def lines_from_file(file_name):
    try:
        my_file = open(file_name, 'r')
        lines = my_file.readlines()
        my_file.close()
    except IOError:
        print("cannot open", file_name)
    return lines

def lines_to_file(file_name, lines):
    try:
        my_file = open(file_name, 'w')
        for line in lines:
            my_file.write(line)
        my_file.close()
    except IOError:
        print("cannot open", file_name)
    return lines

def check_todo(check):
    check_number = int(check)
    file_name = 'todo_list.txt'
    lines = lines_from_file(file_name)
    line = lines[check_number - 1].split(' ')
    line.pop(0)
    line[0] = '[X]'
    lines[check_number - 1] = ' '.join(line)
    lines_to_file(file_name, lines)

def remove_todo(number):
    number = int(number)
    file_name = 'todo_list.txt'
    lines = lines_from_file(file_name)
    lines.pop(number - 1)
    lines_to_file(file_name, lines)

        