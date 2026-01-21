class Todo:
    IS_DONE = 'X'
    NOT_DONE = ' '

    def __init__(self, title):
        self._title = title
        self._done = False
    
    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, value):
        if not isinstance(value, bool):
            raise TypeError('Value given must be boolean')
        
        self._done = value

    def __str__(self):
        mark = Todo.IS_DONE if self.done else Todo.NOT_DONE
        return f'[{mark}] {self.title.capitalize()}'
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return (self.title == other.title) and \
            (self.done == other.done)