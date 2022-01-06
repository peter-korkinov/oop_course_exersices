from ProjectManagment.category import Category
from ProjectManagment.topic import Topic
from ProjectManagment.document import Document


class Storage:
    def __init__(self):
        self.__categories = []
        self.__topics = []
        self.__documents = []

    def __repr__(self):
        return '\n'.join(repr(doc) for doc in self.__documents)

    def add_category(self, category: Category):
        if category not in self.__categories:
            self.__categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.__topics:
            self.__topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.__documents:
            self.__documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        Storage.get_record(category_id, self.__categories).name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_folder: str,):
        topic = Storage.get_record(topic_id, self.__topics)
        topic.topic = new_topic
        topic.storage_folder = new_folder

    def edit_document(self, document_id: int, new_file_name: str):
        Storage.get_record(document_id, self.__documents).file_name = new_file_name

    def delete_category(self, category_id):
        self.__categories.remove(Storage.get_record(category_id, self.__categories))

    def delete_topic(self, topic_id):
        self.__topics.remove(Storage.get_record(topic_id, self.__topics))

    def delete_document(self, document_id):
        self.__documents.remove(Storage.get_record(document_id, self.__documents))

    def get_document(self, document_id):
        return Storage.get_record(document_id, self.__documents)

    @property
    def categories(self):
        return self.__categories

    @property
    def topics(self):
        return self.__topics

    @property
    def documents(self):
        return self.__documents

    @staticmethod
    def get_record(rec_id, target_attr):
        for rec in target_attr:
            if rec.id == rec_id:
                return rec

        raise ValueError('searched item does not exist')
