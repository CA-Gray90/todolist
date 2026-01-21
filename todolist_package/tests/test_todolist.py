import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertIsInstance(self.todos.to_list(), list)
        self.assertEqual([self.todo1, self.todo2, self.todo3],
                         self.todos.to_list())
    
    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())
        self.assertIs(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())
    
    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())
        self.todos.mark_all_undone()
        
        self.todo1.done = True
        self.assertFalse(self.todos.all_done())
        self.todo2.done = True
        self.todo3.done = True
        self.assertTrue(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add('a todo')
        with self.assertRaises(TypeError):
            self.todos.add(1234)
    
    def test_todo_at(self):
        with self.assertRaises(IndexError):
            self.todos.todo_at(3)

        self.assertIs(self.todos.todo_at(1), self.todo2)

    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(3)
        
        self.todos.mark_done_at(0)
        self.assertTrue(self.todo1.done)
    
    def test_mark_done(self):
        self.todos.mark_done('Buy milk')
        self.assertTrue(self.todo1.done)

        with self.assertRaises(TypeError):
            self.todos.mark_done(1)

    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(3)
        
        self.todo1.done = True
        self.todos.mark_undone_at(0)
        self.assertFalse(self.todo1.done)

    def test_mark_all_done(self):
        self.assertFalse(self.todos.all_done())
        
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(3)
        
        self.todos.remove_at(0)
        self.assertNotIn(self.todo1, self.todos.to_list())
        self.assertTrue(len(self.todos) == 2)

    def test_str(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):
        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )

        self.todos.mark_done('Buy milk')
        self.assertEqual(string, str(self.todos))

        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[ ] Go to the gym"
        )

        self.todos.mark_done_at(1)
        self.assertEqual(string, str(self.todos))

    def test_str_all_done_todos(self):
        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )

        self.todos.mark_all_done()
        self.assertEqual(string, str(self.todos))

    def test_each(self):
        result = []
        self.todos.each(lambda todo: result.append(todo))

        self.assertEqual([self.todo1, self.todo2, self.todo3], result)

    def test_select(self):
        new_todos = self.todos.select(lambda todo: not todo.done)
        self.assertEqual(str(new_todos), str(self.todos))

        self.todos.mark_all_done()
        new_todos = self.todos.select(lambda todo: not todo.done)
        self.assertEqual(0, len(new_todos))
    
    def test_find_by_title(self):
        selected = self.todos.find_by_title('Go to the gym')
        self.assertEqual(selected, self.todo3)
    
if __name__ == "__main__":
    unittest.main()