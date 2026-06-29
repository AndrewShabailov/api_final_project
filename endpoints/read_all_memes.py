import requests
import allure
from endpoints.base_meme import BaseMeme


class ReadAllMemes(BaseMeme):

    @allure.step('Send GET request for reading all memes')
    def read_all_memes(self):
        self.response = requests.get(
            f'{self.base_url}/meme', headers=self.headers
        )
        allure.attach(
            self.response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )
        return self.response

    @allure.step('Check that memes list is not empty')
    def check_memes_list_is_not_empty(self):
        response_json = self.json
        assert isinstance(response_json, dict) and 'data' in response_json, \
            "Response should contain a dictionary with 'data' key"
        memes_list = response_json['data']
        assert isinstance(memes_list, list), "Memes data is not a list"
        assert len(memes_list) > 0, "Memes list is empty"
