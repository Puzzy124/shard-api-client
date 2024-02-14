from requests import get
from aiohttp import ClientSession


class TTSResponse:
    def __init__(self, audio: str):
        self.audio = audio

    def __repr__(self):
        return f"<TTSResponse audio={self.audio[:10]}>"

    def __str__(self):
        return f"<TTSResponse audio={self.audio[:10]}>"


class Voice:
    def __init__(self, name: str, labels: dict, preview_url: str):
        self.name = name
        self.age = labels.get("age")
        self.accent = labels.get("accent")
        self.description = labels.get("description")
        self.gender = labels.get("gender")
        self.use_case = labels.get("use_case")
        self.preview_url = preview_url

    def __repr__(self):
        return f"<Voice name={self.name}>"

    def __str__(self):
        return f"<Voice name={self.name}>"


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
        response = get(self.image)
        with open(path, "wb") as file:
            file.write(response.content)

    async def download_async(self, path: str):
        """
        Download the image to a file asynchronously
        """
        async with ClientSession() as session:
            async with session.get(self.image) as response:
                with open(path, "wb") as file:
                    file.write(await response.read())

    def as_bytes(self):
        """
        Return the image as bytes
        """
        response = get(self.image)
        return response.content

    async def as_bytes_async(self):
        """
        Return the image as bytes asynchronously
        """
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
