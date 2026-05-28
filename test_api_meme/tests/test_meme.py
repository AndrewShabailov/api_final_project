import pytest


@pytest.mark.positive
def test_get_all_memes(
        auth_token,
        start_end_testing,
        before_after_testing,
        read_meme_endpoint
):
    read_meme_endpoint.read_meme()
    read_meme_endpoint.check_status_code_is_200()
