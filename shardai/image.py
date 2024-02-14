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

    async def sdxl_completions(
        self,
        prompt: str = None,
        sampler: str = "DPM++ SDE Karras",
        ratio: str = "1024x1024",
        model: str = "dreamshaperXL10_alpha2.safetensors [c8afe2ef]",
        cfg: int = 4,
        steps: int = 15,
        negative_prompt: str = None,
        seed: int = randint(0, 10000000000),
    ):
        """
        SDXL Image generation function
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
                "https://shard-ai.xyz/v1/sdxl/completions",
                json=payload,
                headers=headers,
            ) as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return ImageResponse(
                    json_response["image"],
                    json_response["generation-time"],
                    json_response["warning!"],
                    json_response["info"]["model"],
                )

    async def sdxl_options(self):
        """
        Get available options for SDXL
        """
        async with ClientSession() as session:
            async with session.get("https://shard-ai.xyz/v1/sdxl/models") as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return ImageOptions(
                    json_response["models"],
                    json_response["ratios"],
                    json_response["samplers"],
                    None,
                    json_response["styles"],
                )

    async def turbo_completions(
        self,
        prompt: str = None,
        negative_prompt: str = None,
    ):
        """
        Image generation function for the turbo endpoint
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
        }
        async with ClientSession() as session:
            async with session.post(
                "https://shard-ai.xyz/v1/sdxl-turbo/completions",
                json=payload,
                headers=headers,
            ) as response:
                json_response = await response.json()
                if response.status != 200:
                    raise APIError(f"Error: {response.status}")
                return ImageResponse(
                    json_response["image"],
                    json_response["generation-time"],
                    json_response["warning!"],
                    json_response["info"]["model"],
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

    def sdxl_completions(
        self,
        prompt: str = None,
        sampler: str = "DPM++ SDE Karras",
        ratio: str = "1024x1024",
        model: str = "dreamshaperXL10_alpha2.safetensors [c8afe2ef]",
        cfg: int = 4,
        steps: int = 15,
        negative_prompt: str = None,
        seed: int = randint(0, 10000000000),
    ):
        """
        SDXL Image generation function
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
            "https://shard-ai.xyz/v1/sdxl/completions", json=payload, headers=headers
        )
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return ImageResponse(
            response_json["image"],
            response_json["generation-time"],
            response_json["warning!"],
            response_json["info"]["model"],
        )

    def sdxl_options(self):
        """
        Get available options for SDXL
        """
        response = get("https://shard-ai.xyz/v1/sdxl/models")
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return ImageOptions(
            response_json["models"],
            response_json["ratios"],
            response_json["samplers"],
            None,
            response_json["styles"],
        )

    def turbo_completions(
        self,
        prompt: str = None,
        negative_prompt: str = None,
    ):
        """
        Image generation function for the turbo endpoint
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
        }
        response = get(
            "https://shard-ai.xyz/v1/sdxl-turbo/completions",
            json=payload,
            headers=headers,
        )
        if response.status_code != 200:
            raise APIError(f"Error: {response.status_code}")
        response_json = response.json()
        return ImageResponse(
            response_json["image"],
            response_json["generation-time"],
            response_json["warning!"],
            response_json["info"]["model"],
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
