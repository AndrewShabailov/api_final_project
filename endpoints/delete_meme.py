import requests
import allure
from endpoints.base_meme import BaseMeme


class DeleteMeme(BaseMeme):

    @allure.step('Send DELETE request for deleting meme')
    def delete_meme(self, meme_id):
        self.response = requests.delete(
            f'{self.base_url}/meme/{meme_id}', headers=self.headers
        )
        return self.response
