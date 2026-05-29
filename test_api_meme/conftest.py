import pytest
import requests
from data.payloads import payload
from endpoints.base_meme import BaseMeme
from endpoints.create_meme import CreateMeme
from endpoints.read_meme import ReadMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def create_meme_endpoint(auth_token):
    return CreateMeme(auth_token)

@pytest.fixture()
def read_meme_endpoint(auth_token):
    return ReadMeme(auth_token)

@pytest.fixture()
def delete_meme_endpoint(auth_token):
    return DeleteMeme(auth_token)

@pytest.fixture(scope="session")
def auth_token():
    auth_payload = {"name": "Andrew"}
    response = requests.post(f'{BaseMeme.base_url}/authorize', json=auth_payload).json()
    return response['token']


@pytest.fixture()
def meme_factory(create_meme_endpoint, delete_meme_endpoint):
    created_meme_ids = []

    def _create_meme(custom_payload=payload):
        create_meme_endpoint.create_meme(payload=custom_payload)
        meme_id = create_meme_endpoint.json['id']
        created_meme_ids.append(meme_id)
        return meme_id

    yield _create_meme

    for meme_id in created_meme_ids:
        print(f'\nCleaning up: Deleting meme {meme_id}')
        delete_meme_endpoint.delete_meme(meme_id)


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
