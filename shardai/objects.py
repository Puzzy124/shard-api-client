from base64 import b64encode

from aiohttp import ClientSession
from requests import get


class TTSResponse:

    def __init__(self, audio: str, generation_time: float, warning: str, info: dict):
        self.audio = audio
        self.generation_time = generation_time
        self.warning = warning
        self.model = info.get("model")
        self.language = info.get("language")
        self.gender = info.get("gender")
        self.voice = info.get("voice_used")

    def download(self, path: str):
        """
        Download the audio to a file
        """
        if "https://" not in self.audio:
            self.audio = b64encode(self.audio.replace("data:audio/mp3;base64,", ""))
            with open(path, "wb") as file:
                file.write(self.audio)
        else:
            response = get(self.audio)
            with open(path, "wb") as file:
                file.write(response.content)

    async def download_async(self, path: str):
        """
        Download the audio to a file asynchronously
        """
        if "https://" not in self.audio:
            self.audio = b64encode(self.audio.replace("data:audio/mp3;base64,", ""))
            with open(path, "wb") as file:
                file.write(self.audio)
        else:
            async with ClientSession() as session:
                async with session.get(self.audio) as response:
                    with open(path, "wb") as file:
                        file.write(await response.read())

    def as_bytes(self):
        """
        Return the audio as bytes
        """
        if "https://" not in self.audio:
            return b64encode(self.audio.replace("data:audio/mp3;base64,", ""))
        else:
            response = get(self.audio)
            return response.content

    async def as_bytes_async(self):
        """
        Return the audio as bytes asynchronously
        """
        if "https://" not in self.audio:
            return b64encode(self.audio.replace("data:audio/mp3;base64,", ""))
        else:
            async with ClientSession() as session:
                async with session.get(self.audio) as response:
                    return await response.read()

    def __repr__(self):
        return f"<TTSResponse audio={self.audio[:10]}>"

    def __str__(self):
        return f"<TTSResponse audio={self.audio[:10]}>"


class ElevenLabsVoice:
    def __init__(self, name: str, accent: str, age: str, gender: str, use_case: str):
        self.name = name
        self.accent = accent
        self.age = age
        self.gender = gender
        self.use_case = use_case

    def __repr__(self):
        return f"<ElevenLabsVoice name={self.name}>"

    def __str__(self):
        return f"<ElevenLabsVoice name={self.name}>"


class TikTokVoice:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<TikTokVoice name={self.name}>"

    def __str__(self):
        return f"<TikTokVoice name={self.name}>"


class EdgeVoice:
    def __init__(self, message: str, parameters: dict):
        self.message = message
        self.gender = parameters.get("gender")
        self.language = parameters.get("language")

    def __repr__(self):
        return f"<EdgeVoice message={self.message[:10]}>"

    def __str__(self):
        return f"<EdgeVoice message={self.message[:10]}>"


class GoogleVoice:
    def __init__(self, message: str):
        self.message = message

    def __repr__(self):
        return f"<GoogleVoice message={self.message[:10]}>"

    def __str__(self):
        return f"<GoogleVoice message={self.message[:10]}>"


class ChatResponse:
    def __init__(
        self, id: str, object: str, created: int, model: str, usage: str, choices: dict
    ):
        self.id = id
        self.object = object
        self.created = created
        self.model = model
        self.usage = usage
        self.choices = [
            ChoiceChat(
                choices[0]["message"], choices[0]["finish_reason"], choices[0]["index"]
            )
        ]

    def __repr__(self):
        return f"<ChatResponse id={self.choices[0].message.content[:10]}>"

    def __str__(self):
        return f"<ChatResponse id={self.choices[0].message.content[:10]}>"


class ChoiceChat:
    def __init__(self, message: dict, finish_reason: str, index: int):
        self.message = ChatMessage(message["role"], message["content"])
        self.finish_reason = finish_reason
        self.index = index

    def __repr__(self):
        return f"<ChoiceChat message={self.message.content[:10]}>"

    def __str__(self):
        return f"<ChoiceChat message={self.message.content[:10]}>"


class ChatMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def __repr__(self):
        return f"<ChatMessage content={self.content[:10]}>"

    def __str__(self):
        return f"<ChatMessage content={self.content[:10]}>"


class ImageResponse:

    def __init__(
        self, image: str, generation_time: float, warning: str, info: str = None
    ):
        self.image = image
        self.generation_time = generation_time
        self.warning = warning
        self.info = info

    def download(self, path: str):
        """
        Download the image to a file
        """
        if "https://" not in self.image:
            self.image = b64encode(self.image.replace("data:image/png;base64,", ""))
            with open(path, "wb") as file:
                file.write(self.image)
        else:
            response = get(self.image)
            with open(path, "wb") as file:
                file.write(response.content)

    async def download_async(self, path: str):
        """
        Download the image to a file asynchronously
        """
        if "https://" not in self.image:
            self.image = b64encode(self.image.replace("data:image/png;base64,", ""))
            with open(path, "wb") as file:
                file.write(self.image)
        else:
            async with ClientSession() as session:
                async with session.get(self.image) as response:
                    with open(path, "wb") as file:
                        file.write(await response.read())

    def as_bytes(self):
        """
        Return the image as bytes
        """
        if "https://" not in self.image:
            return b64encode(self.image.replace("data:image/png;base64,", ""))
        else:
            response = get(self.image)
            return response.content

    async def as_bytes_async(self):
        """
        Return the image as bytes asynchronously
        """
        if "https://" not in self.image:
            return b64encode(self.image.replace("data:image/png;base64,", ""))
        else:
            async with ClientSession() as session:
                async with session.get(self.image) as response:
                    return await response.read()

    def __repr__(self):
        return f"<ImageResponse image={self.image[:10]}>"

    def __str__(self):
        return f"<ImageResponse image={self.image[:10]}>"


class ImageOptions:

    def __init__(
        self,
        models: dict,
        ratios: dict,
        samplers: dict,
        upscale: dict = None,
        styles: dict = None,
    ):
        self.models = models
        self.ratios = ratios
        self.samplers = samplers
        self.upscale = upscale
        self.styles = styles

    def __repr__(self):
        return (
            f"<ImageOptions models=... ratios=... samplers=... upscale=...> styles=...>"
        )

    def __str__(self):
        return (
            f"<ImageOptions models=... ratios=... samplers=... upscale=...> styles=...>"
        )


class ModerationResponse:

    def __init__(self, score: str, languages: dict, data: dict):
        self.score = score
        self.language = languages.get("language")
        self.detected_language = languages.get("detected_language")
        self.prompt = data.get("prompt")
        self.attribute = data.get("attribute")
        self.time = data.get("time")

    def __repr__(self):
        return f"<ModerationResponse result={self.score}>"

    def __str__(self):
        return f"<ModerationResponse result={self.score}>"
