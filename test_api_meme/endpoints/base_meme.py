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
            return self.response.json()
        return None

    @allure.step('Check that status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, \
            f'Expected status code 200, but got {self.response.status_code}'
