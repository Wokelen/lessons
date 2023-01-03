from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService
from setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    first = Director(id=1, name='first_director')
    second = Director(id=2, name='second_director')
    third = Director(id=3, name='third_director')

    director_dao.get_one = MagicMock(return_value=first)
    director_dao.get_all = MagicMock(return_value=[first, second, third])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "new_director",
        }
        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "updated_director"
        }
        self.director_service.update(director_d)
