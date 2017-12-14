import unittest
from todo import Todo
from model import Model

class TestTodoApp(unittest.TestCase):
    def test_command_line_input(self):
        todo = Todo()
        self.assertIsInstance(todo.cl_input(), str)

if __name__ == '__main__':
    unittest.main()