from random import randint

from aiohttp import ClientSession
from requests import get

from .exceptions import *
from .objects import ImageOptions, ImageResponse


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
        style: str = "enhance",
        negative_prompt: str = None,
        seed: int = randint(0, 10000000000),
        base64: bool = False,
    ) -> ImageResponse:
        """
        Image generation function

        :param prompt: The prompt for the image
        :param sampler: The sampler to use for the image
        :param ratio: The ratio to use for the image
        :param model: The model to use for the image
        :param cfg: The cfg to use for the image
        :param steps: The steps to use for the image
        :param style: The style to use for the image
        :param negative_prompt: The negative prompt to use for the image
        :param seed: The seed to use for the image
        :param base64: Whether to return the image as base64

        :return: The image response
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
            "style": style,
            "base64": base64,
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
                    json_response["warning!"],
                    json_response["info"]["model"],
                )

    async def options(self) -> ImageOptions:
        """
        Get available options

        :return: The image options
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
        style: str = "enhance",
        negative_prompt: str = None,
        seed: int = randint(0, 10000000000),
        upscale: bool = False,
        base64: bool = False,
    ) -> ImageResponse:
        """
        SDXL Image generation function

        :param prompt: The prompt for the image
        :param sampler: The sampler to use for the image
        :param ratio: The ratio to use for the image
        :param model: The model to use for the image
        :param cfg: The cfg to use for the image
        :param steps: The steps to use for the image
        :param style: The style to use for the image
        :param negative_prompt: The negative prompt to use for the image
        :param seed: The seed to use for the image
        :param upscale: Whether to upscale the image
        :param base64: Whether to return the image as base64

        :return: The image response
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
            "style": "enhance",
            "upscale": upscale,
            "base64": base64,
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

    async def sdxl_options(self) -> ImageOptions:
        """
        Get available options for SDXL

        :return: The image options
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
        style: str = "enhance",
        base64: bool = False,
    ) -> ImageResponse:
        """
        Image generation function for the turbo endpoint

        :param prompt: The prompt for the image
        :param negative_prompt: The negative prompt for the image
        :param style: The style to use for the image
        :param base64: Whether to return the image as base64

        :return: The image response
        """
        if self.api_key is None:
            raise NoAPIKeyError("API key is required for this function")
        if prompt is None:
            raise NoInputError("Prompt is required for this function")
        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "style": style,
            "base64": base64,
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
    ) -> ImageResponse:
        """
        Image generation function

        :param prompt: The prompt for the image
        :param sampler: The sampler to use for the image
        :param ratio: The ratio to use for the image
        :param model: The model to use for the image
        :param cfg: The cfg to use for the image
        :param steps: The steps to use for the image
        :param negative_prompt: The negative prompt to use for the image
        :param seed: The seed to use for the image

        :return: The image response
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
    ) -> ImageResponse:
        """
        SDXL Image generation function

        :param prompt: The prompt for the image
        :param sampler: The sampler to use for the image
        :param ratio: The ratio to use for the image
        :param model: The model to use for the image
        :param cfg: The cfg to use for the image
        :param steps: The steps to use for the image
        :param negative_prompt: The negative prompt to use for the image
        :param seed: The seed to use for the image

        :return: The image response
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

    def sdxl_options(self) -> ImageOptions:
        """
        Get available options for SDXL

        :return: The image options
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
    ) -> ImageResponse:
        """
        Image generation function for the turbo endpoint

        :param prompt: The prompt for the image
        :param negative_prompt: The negative prompt for the image

        :return: The image response
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

    def options(self) -> ImageOptions:
        """
        Get available options

        :return: The image options
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
