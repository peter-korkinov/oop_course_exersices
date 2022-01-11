from ProjectManagment.category import Category
from ProjectManagment.topic import Topic


class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.__id = id
        self.__category_id = category_id
        self.__topic_id = topic_id
        self.__file_name = file_name
        self.__tags = []

    def __repr__(self):
        return f'Document {self.id}: {self.file_name};' \
               f' category {self.category_id},' \
               f' topic {self.topic_id},' \
               f' tags: {", ".join(self.tags)}'

    def add_tag(self, tag_content: str):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id, topic.id, file_name)

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
    def category_id(self):
        return self.__category_id

    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int:
            self.__category_id = category_id
        else:
            raise TypeError('category id must be an integer')

    @property
    def topic_id(self):
        return self.__topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        if type(topic_id) is int:
            self.__topic_id = topic_id
        else:
            raise TypeError('topic id must be an integer')

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        if type(value) is str:
            self.__file_name = value
        else:
            raise TypeError('file name must be mammal string')

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, tag):
        if type(tag) is str:
            self.__tags.append(tag)
        else:
            raise TypeError('tags must be in string format')