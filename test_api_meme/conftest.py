import pytest
import requests
from data.positive_payloads import login_payload  # Имя пользователя 'Andrew' живет тут
from endpoints.auth_meme import AuthMeme
from endpoints.create_meme import CreateMeme


@pytest.fixture(scope='session')
def auth_token():
    auth = AuthMeme(token=None)
    auth.login(login_payload)

    if auth.response.status_code != 200:
        raise RuntimeError(f"Failed to authorize user in session. Status: {auth.response.status_code}")

    token = auth.json.get('token')

    auth.check_token_alive(token)
    if auth.response.status_code != 200:
        raise RuntimeError("Generated token is invalid according to GET /authorize/<token>")

    yield token


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
                f"Fixture failed to setup precondition meme. Status: {creator.response.status_code}"
            )

        meme_id = creator.json.get('id')
        created_meme_ids.append(meme_id)
        return meme_id

    yield _create_meme

    for meme_id in created_meme_ids:
        requests.delete(
            f'http://memesapi.course.qa-practice.com/meme/{meme_id}', headers={'Authorization': auth_token}
        )
