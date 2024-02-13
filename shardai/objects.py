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
    def __init__(self, image: str, generation_time: float, warning: str):
        self.image = image
        self.generation_time = generation_time
        self.warning = warning

    def __repr__(self):
        return f"<ImageResponse image={self.image[:10]}>"

    def __str__(self):
        return f"<ImageResponse image={self.image[:10]}>"


class ImageOptions:

    def __init__(self, models: dict, ratios: dict, samplers: dict, upscale: dict):
        self.models = models
        self.ratios = ratios
        self.samplers = samplers
        self.upscale = upscale

    def __repr__(self):
        return f"<ImageOptions models=... ratios=... samplers=... upscale=...>"

    def __str__(self):
        return f"<ImageOptions models=... ratios=... samplers=... upscale=...>"
