import sys
import model

class Todo(object):
    
    def __init__(self):
        self.inputs = sys.argv
    
    def cl_input(self):
        number_of_args = len(self.inputs)
        if number_of_args == 1:
            model.print_usage()
        else:
            if self.inputs[1] == '-l':
                model.print_todo_list()
            elif self.inputs[1] == '-a':
                model.add_todo(self.inputs[2])
            elif self.inputs[1] == '-c':
                model.check_todo(self.inputs[2])            
    
my_todo = Todo()
my_todo.cl_input()