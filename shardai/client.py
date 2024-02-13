from .chat import ChatAsync, Chat
from .image import ImageAsync, Image
from .tts import TTSAsync, TTS


class ShardClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.chat = Chat(api_key)
        self.chat_async = ChatAsync(api_key)
        self.image = Image(api_key)
        self.image_async = ImageAsync(api_key)
        self.tts = TTS(api_key)
        self.tts_async = TTSAsync(api_key)

    def __repr__(self):
        return f"<ShardClient api_key={self.api_key}>"

    def __str__(self):
        return f"<ShardClient api_key={self.api_key}>"

    def __eq__(self, other):
        return self.api_key == other

    def __ne__(self, other):
        return self.api_key != other

    def __hash__(self):
        return hash(self.api_key)

    def __bool__(self):
        return bool(self.api_key)

    def __len__(self):
        return len(self.api_key)
