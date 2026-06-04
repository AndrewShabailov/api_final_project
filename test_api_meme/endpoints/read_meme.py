import requests
import allure
from endpoints.base_meme import BaseMeme


class ReadMeme(BaseMeme):

    @allure.step('Send GET request for reading special meme')
    def read_meme(self, meme_id):
        self.response = requests.get(
            f'{self.base_url}/meme/{meme_id}', headers=self.headers
        )
        return self.response
