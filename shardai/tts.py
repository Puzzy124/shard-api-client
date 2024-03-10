from aiohttp import ClientSession
from requests import get

from .exceptions import *
from .objects import (EdgeVoice, ElevenLabsVoice, GoogleVoice, TikTokVoice,
                      TTSResponse)


class TTSAsync:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def completions(
        self,
        prompt: str,
        model: str = "ElevenLabs",
        gender: str = "Male",
        language: str = "en",
        voice: str = "Rachel",
    ):
        """
        Text to speech function

        :param prompt: The text to convert to speech
        :param model: The model to use for the text to speech
        :param gender: The gender to use for the text to speech (google and edge)
        :param language: The language to use for the text to speech (google and edge)
        :param voice: The voice to use for the text to speech (elevenlabs and tiktok)

        :return: The audio of the text to speech
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")

        headers = {"api-key": self.api_key}
        if model.lower() in ["google", "edge"]:
            payload = {
                "prompt": prompt,
                "model": model,
                "gender": gender,
                "language": language,
            }
        elif model.lower() in ["elevenlabs", "tiktok"]:
            payload = {
                "prompt": prompt,
                "model": model,
                "voice": voice,
            }
        else:
            raise APIError("Invalid model")
        async with ClientSession() as session:
            async with session.post(
                "https://shard-ai.xyz/v1/tts/completions", json=payload, headers=headers
            ) as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return TTSResponse(
                    json_response["audio"],
                    json_response["generation-time"],
                    json_response["warning!"],
                    json_response["info"],
                )

    async def voices(self):
        """
        Get available voices

        :return: A list of available voices
        """
        async with ClientSession() as session:
            async with session.get("https://shard-ai.xyz/v1/tts/voices") as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return {
                    "elevenlabs": [
                        ElevenLabsVoice(
                            voice["name"],
                            voice["accent"],
                            voice["age"],
                            voice["gender"],
                            voice["use_case"],
                        )
                        for voice in json_response["eleven_labs"]
                    ],
                    "tiktok": [TikTokVoice(voice) for voice in json_response["tiktok"]],
                    "edge": [
                        EdgeVoice(
                            json_response["bing"]["Message"],
                            json_response["bing"]["parameters"],
                        )
                    ],
                    "google": [GoogleVoice(json_response["google"]["Messages"])],
                }


class TTS:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def completions(
        self,
        prompt: str,
        model: str = "ElevenLabs",
        gender: str = "Male",
        language: str = "en",
        voice: str = "Rachel",
    ):
        """
        Text to speech function

        :param prompt: The text to convert to speech
        :param model: The model to use for the text to speech
        :param gender: The gender to use for the text to speech (google and edge)
        :param language: The language to use for the text to speech (google and edge)
        :param voice: The voice to use for the text to speech (elevenlabs and tiktok)

        :return: The audio of the text to speech
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": f"{self.api_key}"}
        if model.lower() in ["google", "edge"]:
            payload = {
                "prompt": prompt,
                "model": model,
                "gender": gender,
                "language": language,
            }
        elif model.lower() in ["elevenlabs", "tiktok"]:
            payload = {
                "prompt": prompt,
                "model": model,
                "voice": voice,
            }
        else:
            raise APIError("Invalid model")
        response = get(
            "https://shard-ai.xyz/v1/tts/completions", json=payload, headers=headers
        )
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return TTSResponse(
            response_json["audio"],
            response_json["generation-time"],
            response_json["warning!"],
            response_json["info"],
        )

    def voices(self):
        """
        Get available voices

        :return: A list of available voices

        
        """
        response = get("https://shard-ai.xyz/v1/tts/voices")
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return {
            "elevenlabs": [
                ElevenLabsVoice(
                    voice["name"],
                    voice["accent"],
                    voice["age"],
                    voice["gender"],
                    voice["use_case"],
                )
                for voice in response_json["eleven_labs"]
            ],
            "tiktok": [TikTokVoice(voice) for voice in response_json["tiktok"]],
            "edge": [
                EdgeVoice(
                    response_json["bing"]["Message"],
                    response_json["bing"]["parameters"],
                )
            ],
            "google": [GoogleVoice(response_json["google"]["Messages"])],
        }
