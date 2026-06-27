payload = {
    "text": "Don't worry about getting older. You're still gonna do dumb stuff, only slower.",
    "url": "https://tenor.com/ru/view/happy-birthday-gif-1289579516793033707",
    "tags": [
        "meme",
        "birthday",
        "funny",
        "aging",
        "humor",
        "sarcasm"
    ],
    "info": {
        "type": "gif",
        "platform": "Tenor",
        "context": "Used as a humorous birthday message about aging",
        "visual_description":
            "A person holding a drink and smiling casually,"
            " with bold white text overlay at the top and bottom delivering a humorous message about aging.",
        "text_format": "uppercase bold impact-style meme font"
    }
}

upd_payload = {
    "text": "My wife told me to stop impersonating a flamingo. I had to put my foot down.",
    "url": "https://tenor.com/view/flamingo-funny-dance-animal-gif-25491840",
    "tags": [
        "meme",
        "pun",
        "funny",
        "flamingo",
        "humor",
        "dad-joke"
    ],
    "info": {
        "type": "gif",
        "platform": "Tenor",
        "context": "Used as a witty dad joke or pun about animals",
        "visual_description":
            "A bright pink flamingo standing on one leg and suddenly doing a goofy dance,"
            " with text overlay explaining the classic pun.",
        "text_format": "clean white sans-serif subtitle font"
    }
}

login_payload = {
    'name': 'Andrew Shabailov'
}

minimal_payload = {
    "text": "One does not simply walk into Mordor.",
    "url": "https://i.imgflip.com/1bij.jpg",
    "tags": ["lotr"],
    "info": {"source": "imgflip"}
}

extra_payload = {
    "text": "I should buy a boat.",
    "url": "https://i.imgflip.com/9ehk.jpg",
    "tags": ["cat", "funny", "meme"],
    "info": {
        "type": "jpg",
        "platform": "imgflip",
        "context": "Classic cat meme about life decisions",
        "text_format": "impact"
    }
}

parametrized_payloads = [
    (
        payload,
        "birthday meme"
    ),
    (
        minimal_payload,
        "minimal payload meme"
    ),
    (
        extra_payload,
        "extra payload meme"
    ),
]
