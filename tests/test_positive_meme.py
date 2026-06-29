import pytest
from data.positive_payloads import payload, upd_payload, minimal_payload, extra_payload, parametrized_payloads
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


@pytest.mark.positive
def test_login_response_contains_token(auth_endpoint):
    auth_endpoint.login(login_payload)
    auth_endpoint.check_status_code_is(200)
    assert 'token' in auth_endpoint.json, "Response does not contain 'token' field"
    assert auth_endpoint.json['token'], "Token value is empty"


@pytest.mark.positive
def test_create_meme_response_contains_all_fields(create_meme_endpoint):
    create_meme_endpoint.create_meme(payload)
    create_meme_endpoint.check_status_code_is(200)
    response = create_meme_endpoint.json
    for field in ('id', 'text', 'url', 'tags', 'info'):
        assert field in response, f"Field '{field}' is missing in create response"


@pytest.mark.positive
def test_get_meme_data_matches_created(meme_factory, create_meme_endpoint, read_meme_endpoint):
    create_meme_endpoint.create_meme(extra_payload)
    create_meme_endpoint.check_status_code_is(200)
    meme_id = create_meme_endpoint.check_meme_id_exists()

    read_meme_endpoint.read_meme(meme_id)
    read_meme_endpoint.check_status_code_is(200)
    read_meme_endpoint.check_response_matches_payload(extra_payload)


@pytest.mark.positive
def test_get_all_memes_contains_created_meme(meme_factory, read_all_memes_endpoint):
    meme_id = meme_factory()
    read_all_memes_endpoint.read_all_memes()
    read_all_memes_endpoint.check_status_code_is(200)
    ids_in_response = [m['id'] for m in read_all_memes_endpoint.json['data']]
    assert meme_id in ids_in_response, f"Created meme id={meme_id} not found in GET /meme list"


@pytest.mark.positive
def test_update_meme_id_unchanged(meme_factory, update_meme_endpoint):
    meme_id = meme_factory()
    update_meme_endpoint.update_meme(payload=upd_payload, meme_id=meme_id)
    update_meme_endpoint.check_status_code_is(200)
    assert int(update_meme_endpoint.json['id']) == int(meme_id), \
        f"Meme id changed after update: expected {meme_id}, got {update_meme_endpoint.json['id']}"


@pytest.mark.positive
def test_delete_meme_response_contains_message(meme_factory, delete_meme_endpoint):
    meme_id = meme_factory()
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_status_code_is(200)
    assert delete_meme_endpoint.response.text, "Delete response body is empty"


@pytest.mark.positive
@pytest.mark.parametrize('test_payload, description', parametrized_payloads)
def test_create_meme_with_various_payloads(create_meme_endpoint, test_payload, description):
    create_meme_endpoint.create_meme(test_payload)
    create_meme_endpoint.check_status_code_is(200)
    create_meme_endpoint.check_meme_id_exists()
    create_meme_endpoint.check_response_matches_payload(test_payload)


@pytest.mark.positive
def test_create_meme_with_minimal_payload(create_meme_endpoint):
    create_meme_endpoint.create_meme(minimal_payload)
    create_meme_endpoint.check_status_code_is(200)
    create_meme_endpoint.check_meme_id_exists()
    create_meme_endpoint.check_response_matches_payload(minimal_payload)


@pytest.mark.positive
def test_update_meme_response_contains_all_fields(meme_factory, update_meme_endpoint):
    meme_id = meme_factory()
    update_meme_endpoint.update_meme(payload=upd_payload, meme_id=meme_id)
    update_meme_endpoint.check_status_code_is(200)
    response = update_meme_endpoint.json
    for field in ('id', 'text', 'url', 'tags', 'info'):
        assert field in response, f"Field '{field}' is missing in update response"
