#from dao.model.director import Director
from my_lessons.HW_18_hard.hard.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, dir_dict):
        data = Director(**dir_dict)
        self.session.add(data)
        self.session.commit()
        return data

    def delete(self,bid):
        director = self.get_one(bid)
        self.session.delete(director)
        self.session.commit()

    def update(self, dir_dict):
        director = self.get_one(dir_dict.get("id"))
        director.name = dir_dict.get("name")
        self.session.add(director)
        self.session.commit()
