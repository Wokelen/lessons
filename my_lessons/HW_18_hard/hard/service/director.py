#from dao.director import DirectorDAO
from my_lessons.HW_18_hard.hard.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, dir_dict):
        return self.dao.create(dir_dict)

    def update(self, dir_dict):
        self.dao.update(dir_dict)
        return self.dao

    def delete(self, bid):
        self.dao.delete(bid)