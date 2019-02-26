import pytest
from main import app
from tinydb import TinyDB
from models.database import client as mongo_client

db_name = "heroku_dt0wvt4m"
mongo_db = mongo_client[db_name]


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    cleanup()  # clean up before every test

    yield client


@pytest.fixture
def client_logged_in():
    app.config['TESTING'] = True
    client = app.test_client()

    cleanup()  # clean up before every test

    # SIGNUP
    password = "password123"
    client.post('/signup', data={"username": "ramuta", "password": password, "repeat": password}, follow_redirects=True)

    yield client


def cleanup():
    # clean up the DB
    db = TinyDB('./localhost/{}.json'.format(db_name))
    db.purge_tables()


def test_signup_login(client):
    # SIGNUP
    password = "password123"
    response_1 = client.post('/signup', data={"username": "ramuta", "password": password,
                                              "repeat": password}, follow_redirects=True)

    assert b'Welcome to Ninja Tech Forum, ramuta' in response_1.data

    # LOGIN
    response_2 = client.post('/login', data={"username": "ramuta", "password": password}, follow_redirects=True)
    assert b'Welcome to Ninja Tech Forum, ramuta' in response_2.data
