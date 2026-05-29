import pytest
from data.payloads import payload


@pytest.mark.positive
def test_get_all_memes(start_end_testing, before_after_testing, read_meme_endpoint):
    read_meme_endpoint.read_meme()
    read_meme_endpoint.check_status_code_is_200()


@pytest.mark.positive
def test_create_meme(start_end_testing, before_after_testing, meme_factory):
    meme_id = meme_factory()
    assert meme_id is not None


@pytest.mark.positive
def test_delete_meme(start_end_testing, before_after_testing, meme_factory, delete_meme_endpoint):
    meme_id = meme_factory()

    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_status_code_is_200()
