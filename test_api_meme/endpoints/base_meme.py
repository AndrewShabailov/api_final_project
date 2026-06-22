import allure


class BaseMeme:
    base_url = 'http://memesapi.course.qa-practice.com'

    def __init__(self, token):
        self.response = None
        self.headers = {
            'Authorization': token
        }

    @property
    def json(self):
        if self.response is not None:
            try:
                return self.response.json()
            except ValueError:
                return None
        return None

    @allure.step('Check that status code is {expected_code}')
    def check_status_code_is(self, expected_code):
        assert self.response.status_code == expected_code, \
            f'Expected {expected_code}, but got {self.response.status_code}'

    @allure.step('Check that meme ID exists in response')
    def check_meme_id_exists(self):
        response_json = self.json
        assert response_json is not None, "Response body is empty or not JSON"
        assert 'id' in response_json, "Field 'id' is missing in response"
        assert response_json['id'] is not None, "Meme ID is None"
        return response_json['id']

    @allure.step('Check that response data matches the sent payload')
    def check_response_matches_payload(self, expected_payload):
        response_json = self.json
        assert response_json is not None, "Response body is empty"
        for key in expected_payload:
            assert response_json.get(key) == expected_payload[key], \
                f"Mismatch in field '{key}': expected {expected_payload[key]}, got {response_json.get(key)}"
