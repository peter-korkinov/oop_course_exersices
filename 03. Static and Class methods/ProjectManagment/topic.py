class Topic:
    def __init__(self, id: int, topic: str, storage_folder: str):
        self.__id = id
        self.__topic = topic
        self.__storage_folder = storage_folder

    def __repr__(self):
        return f'Topic {self.id}: {self.topic} in {self.storage_folder}'

    def edit(self, new_topic, new_folder):
        self.topic = new_topic
        self.storage_folder = new_folder

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
    def topic(self):
        return self.__topic

    @topic.setter
    def topic(self, topic):
        if type(topic) is str:
            self.__topic = topic
        else:
            raise TypeError('topic must be a string')

    @property
    def storage_folder(self):
        return self.__storage_folder

    @storage_folder.setter
    def storage_folder(self, folder):
        if type(folder) is str:
            self.__storage_folder = folder
        else:
            raise TypeError('storage folder must be a string')
