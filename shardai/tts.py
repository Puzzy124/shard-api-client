from requests import get
from aiohttp import ClientSession
from .objects import TTSResponse, Voice
from .exceptions import *


class TTSAsync:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def completions(self, prompt: str, voice: str = "Rachel"):
        """
        Text to speech function
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")

        headers = {"api-key": self.api_key}
        payload = {"prompt": prompt, "voice": voice}
        async with ClientSession() as session:
            async with session.post(
                "https://shard-ai.xyz/v1/tts/completions", json=payload, headers=headers
            ) as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return TTSResponse(json_response["audio"])

    async def voices(self):
        """
        Get available voices
        """
        async with ClientSession() as session:
            async with session.get("https://shard-ai.xyz/v1/tts/voices") as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return [
                    Voice(voice["name"], voice["labels"], voice["preview_url"])
                    for voice in json_response["voices"]
                ]


class TTS:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def completions(self, prompt: str, voice: str = "Rachel"):
        """
        Text to speech function
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": f"{self.api_key}"}
        payload = {"prompt": prompt, "voice": voice}
        response = get(
            "https://shard-ai.xyz/v1/tts/completions", json=payload, headers=headers
        )
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return TTSResponse(response_json["audio"])

    def voices(self):
        """
        Get available voices
        """
        response = get("https://shard-ai.xyz/v1/tts/voices")
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return [
            Voice(voice["name"], voice["labels"], voice["preview_url"])
            for voice in response_json["voices"]
        ]
