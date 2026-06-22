import pytest
import requests

from data.positive_payloads import login_payload
from endpoints.auth_meme import AuthMeme
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.read_all_memes import ReadAllMemes
from endpoints.read_meme import ReadMeme
from endpoints.delete_meme import DeleteMeme  # Добавили импорт класса удаления


@pytest.fixture(scope='session')
def auth_token():
    auth = AuthMeme(token=None)
    auth.login(login_payload)

    if auth.response.status_code != 200:
        raise RuntimeError(
            f"Failed to authorize user in session. "
            f"Status: {auth.response.status_code}"
        )

    token = auth.json.get('token')

    auth.check_token_alive(token)
    if auth.response.status_code != 200:
        raise RuntimeError(
            "Generated token is invalid according to GET /authorize/<token>"
        )

    yield token


@pytest.fixture()
def auth_endpoint(auth_token):
    return AuthMeme(token=auth_token)


@pytest.fixture()
def create_meme_endpoint(auth_token):
    return CreateMeme(token=auth_token)


@pytest.fixture()
def update_meme_endpoint(auth_token):
    return UpdateMeme(token=auth_token)


@pytest.fixture()
def read_meme_endpoint(auth_token):
    return ReadMeme(token=auth_token)


@pytest.fixture()
def read_all_memes_endpoint(auth_token):
    return ReadAllMemes(token=auth_token)


@pytest.fixture()
def delete_meme_endpoint(auth_token):
    return DeleteMeme(token=auth_token)


@pytest.fixture()
def meme_factory(auth_token):
    created_meme_ids = []

    def _create_meme():
        payload = {
            "text": "Factory Meme",
            "url": "http://example.com/factory.jpg",
            "tags": ["factory"],
            "info": {"source": "fixture"}
        }
        creator = CreateMeme(token=auth_token)
        creator.create_meme(payload)

        if creator.response.status_code != 200:
            raise RuntimeError(
                f"Fixture failed to setup precondition meme. "
                f"Status: {creator.response.status_code}"
            )

        meme_id = creator.json.get('id')
        created_meme_ids.append(meme_id)
        return meme_id

    yield _create_meme

    for meme_id in created_meme_ids:
        requests.delete(
            f'http://memesapi.course.qa-practice.com/meme/{meme_id}',
            headers={'Authorization': auth_token}
        )
