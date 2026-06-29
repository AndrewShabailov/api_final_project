# 1. missing required fields
meme_missing_text = {"url": "http://..", "tags": ["funny"], "info": {"type": "gif"}}
meme_missing_url = {"text": "Meme text", "tags": ["funny"], "info": {"type": "gif"}}
meme_missing_tags = {"text": "Meme text", "url": "http://..", "info": {"type": "gif"}}
meme_missing_info = {"text": "Meme text", "url": "http://..", "tags": ["funny"]}
meme_empty_body = {}

# 2. wrong type
meme_text_as_int = {"text": 12345, "url": "http://..", "tags": ["funny"], "info": {"type": "gif"}}
meme_url_as_list = {"text": "Text", "url": ["http://.."], "tags": ["funny"], "info": {"type": "gif"}}
meme_tags_as_string = {"text": "Text", "url": "http://..", "tags": "not_an_array", "info": {"type": "gif"}}
meme_info_as_string = {"text": "Text", "url": "http://..", "tags": ["funny"], "info": "not_an_object"}

# 3. wrong validation
meme_empty_fields = {"text": "", "url": "", "tags": [], "info": {}}

# 4. negative validation
login_empty_name = {'name': ''}
login_int_name = {'name': 12345}
login_missing_name = {}
