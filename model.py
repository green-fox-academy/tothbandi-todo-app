class Model(object):

    def __init__(self):
        self.file_name = 'todo_list.txt'

    def print_usage(self):
        print('''Command Line Todo application
    =============================

    Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task''')

    def print_todo_list(self):
        try:
            my_file = open(self.file_name, 'r')
            lines = my_file.readlines()
            if len(lines) == 0:
                print('No todos for today! :)')
            else:
                for i in range(len(lines)):
                    print('{} - {}'.format(i + 1, lines[i]), end='')
                print()
            my_file.close()
        except IOError:
            print('cannot open', self.file_name)

    def add_todo(self, task):
        try:
            my_file = open(self.file_name, 'a')
            my_file.write('\n[ ] ' + task )
            my_file.close()
        except IOError:
            print('cannot open', self.file_name)

    def lines_from_file(self):
        try:
            my_file = open(self.file_name, 'r')
            lines = my_file.readlines()
            my_file.close()
        except IOError:
            print("cannot open", self.file_name)
        return lines

    def lines_to_file(self, lines):
        try:
            my_file = open(self.file_name, 'w')
            for line in lines:
                my_file.write(line)
            my_file.close()
        except IOError:
            print("cannot open", self.file_name)
        return lines

    def check_todo(self, check):
        check_number = int(check)
        lines = self.lines_from_file()
        if check_number <= len(lines) and check_number > 0:
            line = lines[check_number - 1].split(' ')
            if line[0].upper() != '[X]':
                line.pop(0)
                line[0] = '[X]'
            else:
                line[0] = '[ ]'
            lines[check_number - 1] = ' '.join(line)
            self.lines_to_file(lines)        
        else:
            print('Unable to check: index is out of bound')
            self.print_usage()    

    def remove_todo(self, number):
        number = int(number)
        lines = self.lines_from_file()
        if number <= len(lines) and number > 0:
            lines.pop(number - 1)
            if lines[-1][-1] == '\n':
                lines[-1] = lines[-1][:-1]
            self.lines_to_file(lines)       
        else:
            print('Unable to remove: index is out of bound')
            self.print_usage()
 

        