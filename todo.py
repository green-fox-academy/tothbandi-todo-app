import sys
import model

class Todo(object):
    
    def __init__(self):
        self.inputs = sys.argv
    
    def cl_input(self):
        if len(self.inputs) == 1:
            model.print_usage()
        else:
            if self.inputs[1] == '-l':
                model.print_todo_list()
    
my_todo = Todo()
my_todo.cl_input()