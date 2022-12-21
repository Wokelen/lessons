from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, gen_dict):
        data = Genre(**gen_dict)
        self.session.add(data)
        self.session.commit()
        return data

    def delete(self,bid):
        genre = self.get_one(bid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, gen_dict):
        genre = self.get_one(gen_dict.get("id"))
        genre.name = gen_dict.get("name")
        self.session.add(genre)
        self.session.commit()