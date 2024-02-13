from .objects import ImageResponse, ImageOptions
from requests import get
from aiohttp import ClientSession
from random import randint
from .exceptions import *


class ImageAsync:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def completions(
        self,
        prompt: str = None,
        sampler: str = "DPM++ SDE Karras",
        ratio: str = "square",
        model: str = "DREAMSHAPER_8",
        cfg: int = 4,
        steps: int = 15,
        negative_prompt: str = None,
        seed: int = randint(0, 10000000000),
    ):
        """
        Image generation function
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {
            "prompt": prompt,
            "sampler": sampler,
            "ratio": ratio,
            "model": model,
            "cfg": cfg,
            "steps": steps,
            "negative_prompt": negative_prompt,
            "seed": seed,
        }
        async with ClientSession() as session:
            async with session.post(
                "https://shard-ai.xyz/v1/sd1x/completions",
                json=payload,
                headers=headers,
            ) as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return ImageResponse(
                    json_response["image"],
                    json_response["generation-time"],
                    json_response["Warning!"],
                )

    async def options(self):
        """
        Get available options
        """
        async with ClientSession() as session:
            async with session.get("https://shard-ai.xyz/v1/sd1x/models") as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return ImageOptions(
                    json_response["models"],
                    json_response["ratios"],
                    json_response["samplers"],
                    json_response["upscale"],
                )


class Image:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def completions(
        self,
        prompt: str = None,
        sampler: str = "DPM++ SDE Karras",
        ratio: str = "square",
        model: str = "DREAMSHAPER_8",
        cfg: int = 4,
        steps: int = 15,
        negative_prompt: str = None,
        seed: int = randint(0, 10000000000),
    ):
        """
        Image generation function
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {
            "prompt": prompt,
            "sampler": sampler,
            "ratio": ratio,
            "model": model,
            "cfg": cfg,
            "steps": steps,
            "negative_prompt": negative_prompt,
            "seed": seed,
        }
        response = get(
            "https://shard-ai.xyz/v1/sd1x/completions", json=payload, headers=headers
        )
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return ImageResponse(
            response_json["image"],
            response_json["generation-time"],
            response_json["Warning!"],
        )

    def options(self):
        """
        Get available options
        """
        response = get("https://shard-ai.xyz/v1/sd1x/models")
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return ImageOptions(
            response_json["models"],
            response_json["ratios"],
            response_json["samplers"],
            response_json["upscale"],
        )
