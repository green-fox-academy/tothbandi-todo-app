import sys
import model

class Todo(object):

    def __init__(self):
        self.my_model = model.Model()

    def arguments_validator(self):
        if len(sys.argv) == 1:
            return True
        elif len(sys.argv) == 2:
            if sys.argv[1] == '-l':
                return True
            elif sys.argv[1] == '-a':
                print('Unable to add: no task provided')
            elif sys.argv[1] == '-c':
                print('Unable to check: no index provided')
            elif sys.argv[1] == '-r':
                print('Unable to remove: no index provided')                    
            else:
                print('Unsupported argument\n')
        elif len(sys.argv) == 3:
            if sys.argv[1] == '-a':
                return True
            elif sys.argv[1] == '-c' or sys.argv[1] == '-r':
                if sys.argv[2].isdigit():
                    return True
                else:
                    print('Unable to remove: index is not a number')
            else:
                print('Unsupported argument\n')
        return False

    def command_line_input(self):
        if self.arguments_validator():
            if len(sys.argv) == 1:
                self.my_model.print_usage()
            else:
                if sys.argv[1] == '-l':
                    self.my_model.print_todo_list()
                elif sys.argv[1] == '-a':
                    self.my_model.add_todo(sys.argv[2])
                elif sys.argv[1] == '-c':
                    self.my_model.check_todo(sys.argv[2])            
                elif sys.argv[1] == '-r':
                    self.my_model.remove_todo(sys.argv[2])
        else:
            self.my_model.print_usage()
        
my_todo = Todo()
my_todo.command_line_input()