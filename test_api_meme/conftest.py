import pytest
import requests
from endpoints.read_meme import ReadMeme
from endpoints.base_meme import BaseMeme


@pytest.fixture()
def read_meme_endpoint(auth_token):
    return ReadMeme(auth_token)


@pytest.fixture(scope="session")
def auth_token():
    payload = {"name": "Andrew"}
    response = requests.post(f'{BaseMeme.base_url}/authorize', json=payload).json()
    return response['token']


@pytest.fixture(scope='session')
def start_end_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after_testing():
    print('Before test')
    yield
    print('After test')
