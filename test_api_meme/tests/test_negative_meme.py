import pytest
from endpoints.read_meme import ReadMeme
from endpoints.auth_meme import AuthMeme
from data import negative_payloads as bad


@pytest.mark.negative
@pytest.mark.parametrize("bad_login", [bad.login_int_name, bad.login_missing_name])
def test_login_invalid_data_returns_400(auth_endpoint, bad_login):
    auth_endpoint.login(bad_login)
    auth_endpoint.check_status_code_is(400)


@pytest.mark.bug(reason="Status code should be 400 but got 200")
@pytest.mark.negative
def test_login_empty_name_bug(auth_endpoint):
    auth_endpoint.login(bad.login_empty_name)
    auth_endpoint.check_status_code_is(200)


@pytest.mark.bug(reason="Status code should be 401 Unauthorized but got 404")
@pytest.mark.negative
@pytest.mark.parametrize("invalid_token", ["wrong_token_123", "", "None"])
def test_check_token_alive_with_invalid_token(invalid_token):
    endpoint = AuthMeme(token=invalid_token)
    endpoint.check_token_alive(invalid_token)
    endpoint.check_status_code_is(401)


@pytest.mark.bug(reason="Status code should be 401 Unauthorized but got 404")
@pytest.mark.negative
def test_get_all_memes_without_token():
    endpoint = AuthMeme(token=None)
    endpoint.check_token_alive(token=None)
    endpoint.check_status_code_is(401)


@pytest.mark.negative
@pytest.mark.parametrize("bad_payload", [
    bad.meme_missing_text,
    bad.meme_missing_url,
    bad.meme_missing_tags,
    bad.meme_missing_info,
    bad.meme_empty_body,
    bad.meme_text_as_int,
    bad.meme_url_as_list,
    bad.meme_tags_as_string,
    bad.meme_info_as_string
])
def test_create_meme_invalid_data_returns_400(create_meme_endpoint, bad_payload):
    create_meme_endpoint.create_meme(payload=bad_payload)
    create_meme_endpoint.check_status_code_is(400)


@pytest.mark.bug(reason="Payload with empty fields got 200 instead of 400")
@pytest.mark.negative
def test_create_meme_empty_fields_bug(create_meme_endpoint):
    create_meme_endpoint.create_meme(payload=bad.meme_empty_fields)
    create_meme_endpoint.check_status_code_is(200)


@pytest.mark.negative
@pytest.mark.parametrize("fake_id", [999999, 0, -50, "not_an_id"])
def test_get_single_meme_negative(read_meme_endpoint, fake_id):
    read_meme_endpoint.read_meme(meme_id=fake_id)
    read_meme_endpoint.check_status_code_is(404)


@pytest.mark.negative
@pytest.mark.parametrize("bad_put_payload", [bad.meme_missing_text, bad.meme_text_as_int])
def test_update_meme_invalid_data_returns_400(meme_factory, update_meme_endpoint, bad_put_payload):
    meme_id = meme_factory()
    update_meme_endpoint.update_meme(payload=bad_put_payload, meme_id=meme_id)
    update_meme_endpoint.check_status_code_is(400)


@pytest.mark.bug(reason="Payload with empty fields got 200 instead of 400")
@pytest.mark.negative
def test_update_meme_empty_fields_bug(meme_factory, update_meme_endpoint):
    meme_id = meme_factory()
    update_meme_endpoint.update_meme(payload=bad.meme_empty_fields, meme_id=meme_id)
    update_meme_endpoint.check_status_code_is(200)


@pytest.mark.negative
def test_update_non_existent_meme(update_meme_endpoint):
    fake_id = 999999
    valid_payload_structure = {
        "id": fake_id, "text": "Valid", "url": "http://..", "tags": [], "info": {}
    }
    update_meme_endpoint.update_meme(payload=valid_payload_structure, meme_id=fake_id)
    update_meme_endpoint.check_status_code_is(404)


@pytest.mark.negative
@pytest.mark.parametrize("invalid_id", [999999, 0, -1, "abc"])
def test_delete_meme_negative(delete_meme_endpoint, invalid_id):
    delete_meme_endpoint.delete_meme(invalid_id)
    delete_meme_endpoint.check_status_code_is(404)
