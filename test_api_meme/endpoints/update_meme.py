import requests
import allure
from endpoints.base_meme import BaseMeme


class UpdateMeme(BaseMeme):

    @allure.step('Send PUT request for updating meme')
    def update_meme(self, payload, meme_id):
        full_payload = payload.copy()
        full_payload['id'] = int(meme_id)

        self.response = requests.put(
            f'{self.base_url}/meme/{meme_id}', json=full_payload, headers=self.headers
        )
        allure.attach(
            self.response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )
        return self.response
