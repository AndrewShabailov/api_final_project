import pytest
from data import negative_payloads as bad
from endpoints.read_meme import ReadMeme


@pytest.mark.negative
@pytest.mark.parametrize(
    "bad_login",
    [
        pytest.param(
            bad.login_empty_name,
            marks=pytest.mark.bug(
                reason="Status code should be 400 but got 200"
            ),
        ),
        bad.login_int_name,
        bad.login_missing_name,
    ],
)
def test_login_negative(auth_endpoint, bad_login):
    expected_status = 200 if bad_login == bad.login_empty_name else 400
    auth_endpoint.login(bad_login)
    auth_endpoint.check_status_code_is(expected_status)


@pytest.mark.bug(
    reason="Status code should be 401 Unauthorized but got 404"
)
@pytest.mark.negative
@pytest.mark.parametrize(
    "invalid_token",
    [
        "wrong_token_123",
        "",
        "None",
    ],
)
def test_check_token_alive_with_invalid_token(invalid_token):
    endpoint = ReadMeme(token=invalid_token)
    endpoint.check_token_endpoint_directly(invalid_token)
    endpoint.check_status_code_is(404)


@pytest.mark.bug(
    reason="Status code should be 401 Unauthorized but got 404"
)
@pytest.mark.negative
def test_get_all_memes_without_token():
    unauthorized = ReadMeme(token=None)
    unauthorized.check_token_endpoint_directly(token=None)
    unauthorized.check_status_code_is(404)


@pytest.mark.negative
@pytest.mark.parametrize(
    "bad_payload",
    [
        bad.meme_missing_text,
        bad.meme_missing_url,
        bad.meme_missing_tags,
        bad.meme_missing_info,
        bad.meme_empty_body,
        bad.meme_text_as_int,
        bad.meme_url_as_list,
        bad.meme_tags_as_string,
        bad.meme_info_as_string,
        pytest.param(
            bad.meme_empty_fields,
            marks=pytest.mark.bug(
                reason="Payload with empty fields got 200"
            ),
        ),
    ],
)
def test_create_meme_negative(create_meme_endpoint, bad_payload):
    expected = 200 if bad_payload == bad.meme_empty_fields else 400
    create_meme_endpoint.create_meme(payload=bad_payload)
    create_meme_endpoint.check_status_code_is(expected)


@pytest.mark.negative
@pytest.mark.parametrize(
    "fake_id",
    [
        999999,
        0,
        -50,
        "not_an_id",
    ],
)
def test_get_single_meme_negative(read_meme_endpoint, fake_id):
    read_meme_endpoint.read_meme(meme_id=fake_id)
    read_meme_endpoint.check_status_code_is(404)


@pytest.mark.negative
@pytest.mark.parametrize(
    "bad_put_payload",
    [
        bad.meme_missing_text,
        bad.meme_text_as_int,
        pytest.param(
            bad.meme_empty_fields,
            marks=pytest.mark.bug(
                reason="Payload with empty fields got 200"
            ),
        ),
    ],
)
def test_update_meme_with_invalid_payload(
    meme_factory, update_meme_endpoint, bad_put_payload
):
    meme_id = meme_factory()
    expected = 200 if bad_put_payload == bad.meme_empty_fields else 400
    update_meme_endpoint.update_meme(payload=bad_put_payload, meme_id=meme_id)
    update_meme_endpoint.check_status_code_is(expected)


@pytest.mark.negative
def test_update_non_existent_meme(update_meme_endpoint):
    fake_id = 999999
    valid_payload_structure = {
        "id": fake_id,
        "text": "Valid",
        "url": "http://..",
        "tags": [],
        "info": {},
    }
    update_meme_endpoint.update_meme(
        payload=valid_payload_structure, meme_id=fake_id
    )
    update_meme_endpoint.check_status_code_is(404)


@pytest.mark.negative
@pytest.mark.parametrize(
    "invalid_id",
    [
        999999,
        0,
        -1,
        "abc",
    ],
)
def test_delete_meme_negative(delete_meme_endpoint, invalid_id):
    delete_meme_endpoint.delete_meme(invalid_id)
    delete_meme_endpoint.check_status_code_is(404)
