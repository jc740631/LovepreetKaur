"""..."""


# Create your Place class in this file


class Place:
    name = ''
    country = ''
    priority = 0
    is_visited = ''

    # def __init__(self):
    #     self.name = ''
    #     self.country = ''
    #     self.priority = 0
    #     self.is_visited = ''

    def __init__(self, name='', country='', priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def mark_visited(self):
        self.is_visited = True

    def mark_unvisited(self):
        self.is_visited = False

    def check_important(self):
        if self.priority <= 2:
            if self.is_visited:
                print(f'You need to visit {self.name}. Get going! ')
            else:
                print(f'you visited {self.name}. Great travelling!')
        else:
            print('invalid priority')

    def __str__(self):
        return f'{self.name} in {self.country}, priority {self.priority}'
