from unittest.mock import MagicMock
import pytest
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    first = Movie(id=1, title='fst_title', description="fst_descr",
                  trailer="fst_tr", year=2000, rating=8.6, genre_id=2, director_id=1)
    second = Movie(id=2, title='snd_title', description="snd_descr",
                   trailer="snd_tr", year=2010, rating=8.9, genre_id=1, director_id=3)
    third = Movie(id=3, title='thd_title', description="thd_descr",
                  trailer="thd_tr", year=2015, rating=7.6, genre_id=3, director_id=2)

    movie_dao.get_one = MagicMock(return_value=first)
    movie_dao.get_all = MagicMock(return_value=[first, second, third])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "new_title",
            "description": "new_description",
            "trailer": "new_trailer",
            "year": 1965,
            "genre_id": 2,
            "director_id": 1
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "updated_title",
            "description": "updated_description",
            "trailer": "updated_trailer",
            "year": 1965,
            "genre_id": 2,
            "director_id": 1
        }
        self.movie_service.update(movie_d)
