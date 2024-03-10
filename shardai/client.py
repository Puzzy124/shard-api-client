from .chat import Chat, ChatAsync
from .image import Image, ImageAsync
from .moderation import Moderation, ModerationAsync
from .tts import TTS, TTSAsync


class ShardClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.chat = Chat(api_key)
        self.chat_async = ChatAsync(api_key)
        self.image = Image(api_key)
        self.image_async = ImageAsync(api_key)
        self.tts = TTS(api_key)
        self.tts_async = TTSAsync(api_key)
        self.moderation = Moderation(api_key)
        self.moderation_async = ModerationAsync(api_key)

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
