class Category:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    def __repr__(self):
        return f'Category {self.id}: {self.name}'

    def edit(self, new_name: str):
        self.name = new_name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if type(id) is int:
            self.__id = id
        else:
            raise TypeError('id must be an integer')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name
        else:
            raise TypeError('name must be mammal string')
