class TTSResponse:
    def __init__(self, audio):
        self.audio = audio


class Voice:
    def __init__(self, name, labels, preview_url):
        self.name = name
        self.age = labels.get("age")
        self.accent = labels.get("accent")
        self.description = labels.get("description")
        self.gender = labels.get("gender")
        self.use_case = labels.get("use_case")
        self.preview_url = preview_url


class ChatResponse:
    def __init__(self, id, object, created, model, usage, choices):
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


class ChoiceChat:
    def __init__(self, message: dict, finish_reason, index):
        self.message = ChatMessage(message["role"], message["content"])
        self.finish_reason = finish_reason
        self.index = index


class ChatMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content


class ImageResponse:
    def __init__(self, image, generation_time, warning):
        self.image = image
        self.generation_time = generation_time
        self.warning = warning


class ImageOptions:
    def __init__(self, models, ratios, samplers, upscale):
        self.models = models
        self.ratios = ratios
        self.samplers = samplers
        self.upscale = upscale
