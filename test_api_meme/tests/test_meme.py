import pytest
from data.payloads import payload, upd_payload


@pytest.mark.positive
def test_get_all_memes(read_meme_endpoint):
    read_meme_endpoint.read_meme()
    read_meme_endpoint.check_status_code_is_200()


@pytest.mark.positive
def test_token_is_alive(read_meme_endpoint):
    read_meme_endpoint.check_token()
    read_meme_endpoint.check_status_code_is_200()


@pytest.mark.positive
def test_create_meme(meme_factory):
    meme_id = meme_factory()
    assert meme_id is not None


@pytest.mark.positive
def test_update_meme(meme_factory, update_meme_endpoint):
    meme_id = meme_factory()

    update_meme_endpoint.update_meme(payload=upd_payload, meme_id=meme_id)
    update_meme_endpoint.check_status_code_is_200()


@pytest.mark.positive
def test_delete_meme(meme_factory, delete_meme_endpoint):
    meme_id = meme_factory()

    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_status_code_is_200()
