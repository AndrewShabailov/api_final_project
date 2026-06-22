import pytest
from data.positive_payloads import payload, upd_payload
from endpoints.auth_meme import AuthMeme
from data.positive_payloads import login_payload


@pytest.mark.positive
def test_get_all_memes(read_all_memes_endpoint):
    read_all_memes_endpoint.read_all_memes()
    read_all_memes_endpoint.check_status_code_is(200)
    read_all_memes_endpoint.check_memes_list_is_not_empty()


@pytest.mark.positive
def test_get_meme(read_meme_endpoint, meme_factory):
    meme_id = meme_factory()
    read_meme_endpoint.read_meme(meme_id)
    read_meme_endpoint.check_status_code_is(200)
    read_meme_endpoint.check_meme_id_exists()


@pytest.mark.positive
def test_token_is_alive(auth_token):
    endpoint = AuthMeme(token=auth_token)
    endpoint.check_token_alive(auth_token)
    endpoint.check_status_code_is(200)


@pytest.mark.positive
def test_login(auth_endpoint):
    auth_endpoint.login(login_payload)
    auth_endpoint.check_status_code_is(200)


@pytest.mark.positive
def test_create_meme(create_meme_endpoint):
    create_meme_endpoint.create_meme(payload)
    create_meme_endpoint.check_status_code_is(200)
    create_meme_endpoint.check_meme_id_exists()
    create_meme_endpoint.check_response_matches_payload(payload)


@pytest.mark.positive
def test_update_meme(meme_factory, update_meme_endpoint):
    meme_id = meme_factory()
    update_meme_endpoint.update_meme(payload=upd_payload, meme_id=meme_id)
    update_meme_endpoint.check_status_code_is(200)
    update_meme_endpoint.check_response_matches_payload(upd_payload)


@pytest.mark.positive
def test_delete_meme(meme_factory, delete_meme_endpoint, read_meme_endpoint):
    meme_id = meme_factory()
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_status_code_is(200)

    read_meme_endpoint.read_meme(meme_id)
    read_meme_endpoint.check_status_code_is(404)
