import sys
import model

def arguments_validator():
    if len(sys.argv) == 1:
        return True
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-l':
            return True
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-a':
            return True
        elif sys.argv[1] == '-c' or sys.argv[1] == '-r':
            if sys.argv[2].isdigit():
                return True
    return False

def cl_input():
    if arguments_validator():
        if len(sys.argv) == 1:
            model.print_usage()
        else:
            if sys.argv[1] == '-l':
                model.print_todo_list()
            elif sys.argv[1] == '-a':
                model.add_todo(sys.argv[2])
            elif sys.argv[1] == '-c':
                model.check_todo(sys.argv[2])            
            elif sys.argv[1] == '-r':
                model.remove_todo(sys.argv[2])
    else:
        print('Unsupported argument\n')
        model.print_usage()
        
cl_input()