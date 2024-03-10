from aiohttp import ClientSession
from requests import get

from .exceptions import *
from .objects import ModerationResponse


class ModerationAsync:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def completions(self, prompt: str, attribute: str = "TOXICITY") -> dict:
        """
        Moderation function

        :param prompt: The prompt to use for the moderation
        :param attribute: The attribute to use for the moderation

        :return: The response of the moderation
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")

        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {"prompt": prompt, "attribute": attribute}
        async with ClientSession() as session:
            async with session.post(
                "https://shard-ai.xyz/v1/moderation/completions",
                json=payload,
                headers=headers,
            ) as response:
                print(await response.text())
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return ModerationResponse(
                    json_response["score"],
                    json_response["languages"],
                    json_response["data"],
                )

    async def attributes(self) -> list:
        """
        Get available attributes

        :return: The available attributes
        """
        async with ClientSession() as session:
            async with session.get(
                "https://shard-ai.xyz/v1/moderation/attributes"
            ) as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return json_response["attribute"]


class Moderation:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def completions(self, prompt: str, attribute: str = "TOXICITY") -> ModerationResponse:
        """
        Moderation function

        :param prompt: The prompt to use for the moderation
        :param attribute: The attribute to use for the moderation

        :return: The response of the moderation
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")

        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {"prompt": prompt, "attribute": attribute}
        response = get(
            "https://shard-ai.xyz/v1/moderation/completions",
            json=payload,
            headers=headers,
        )
        json_response = response.json()
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        return ModerationResponse(
            json_response["score"],
            json_response["languages"],
            json_response["data"],
        )

    def attributes(self) -> list:
        """
        Get available attributes

        :return: The available attributes
        """
        response = get("https://shard-ai.xyz/v1/moderation/attributes")
        json_response = response.json()
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        return json_response["attribute"]
