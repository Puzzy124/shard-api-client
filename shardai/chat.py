from aiohttp import ClientSession
from requests import get

from .exceptions import *
from .objects import ChatResponse


class ChatAsync:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def completions(
        self, model: str, messages: list = None, prompt: str = None
    ) -> ChatResponse:
        """
        Chat function

        :param prompt: The prompt to use for the chat
        :param model: The model to use for the chat

        :return: The response of the chat
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")

        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = (
            {"messages": [{"role": "user", "content": prompt}], "model": model}
            if messages is None
            else {"messages": messages, "model": model}
        )
        async with ClientSession() as session:
            async with session.post(
                "https://shard-ai.xyz/v1/chat/completions",
                json=payload,
                headers=headers,
            ) as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return ChatResponse(
                    json_response["id"],
                    json_response["object"],
                    json_response["created"],
                    json_response["model"],
                    json_response["usage"],
                    json_response["choices"],
                )

    async def models(self) -> list:
        """
        Get available models

        :return: The available models
        """
        async with ClientSession() as session:
            async with session.get("https://shard-ai.xyz/v1/chat/models") as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return json_response["models"]


class Chat:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def completions(
        self, model: str, messages: list = None, prompt: str = None
    ) -> ChatResponse:
        """
        Chat function

        :param prompt: The prompt to use for the chat
        :param model: The model to use for the chat

        :return: The response of the chat
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = (
            {"messages": [{"role": "user", "content": prompt}], "model": model}
            if messages is None
            else {"messages": messages, "model": model}
        )
        response = get(
            "https://shard-ai.xyz/v1/chat/completions", json=payload, headers=headers
        )
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return ChatResponse(
            response_json["id"],
            response_json["object"],
            response_json["created"],
            response_json["model"],
            response_json["usage"],
            response_json["choices"],
        )

    def models(self) -> list:
        """
        Get available models

        :return: The available models
        """
        response = get("https://shard-ai.xyz/v1/chat/models")
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return response_json["models"]
