import pytest
from endpoints.base_endpoint import Base


@pytest.mark.positive
def test_get_all_memes(
        start_end_testing,
        before_after_testing,
):
    get_meme.check_status_code_is_200()
