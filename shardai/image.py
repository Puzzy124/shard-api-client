from .objects import ImageResponse, ImageOptions
from requests import get
from aiohttp import ClientSession
from random import randint


def completions(
    prompt: str = None,
    sampler: str = "DPM++ SDE Karras",
    ratio: str = "square",
    model: str = "DREAMSHAPER_8",
    cfg: int = 4,
    steps: int = 15,
    negative_prompt: str = None,
    seed: int = randint(0, 10000000000),
    api_key: str = None,
):
    """
    Image generation function
    """
    if api_key is None:
        raise ValueError("API key is required for this function")
    if prompt is None:
        raise ValueError("Prompt is required for this function")
    headers = {"api-key": api_key, "Content-Type": "application/json"}
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
        raise ValueError(f"Error: {response.status_code}")
    response_json = response.json()
    return ImageResponse(
        response_json["image"],
        response_json["generation-time"],
        response_json["Warning!"],
    )


async def completions_async(
    prompt: str = None,
    sampler: str = "DPM++ SDE Karras",
    ratio: str = "square",
    model: str = "DREAMSHAPER_8",
    cfg: int = 4,
    steps: int = 15,
    negative_prompt: str = None,
    seed: int = randint(0, 10000000000),
    api_key: str = None,
):
    """
    Image generation function
    """
    if api_key is None:
        raise ValueError("API key is required for this function")
    if prompt is None:
        raise ValueError("Prompt is required for this function")
    headers = {"api-key": api_key, "Content-Type": "application/json"}
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
            "https://shard-ai.xyz/v1/sd1x/completions", json=payload, headers=headers
        ) as response:
            json_response = await response.json()
            if response.status != 200:
                raise ValueError(f"Error: {response.status}")
            return ImageResponse(
                json_response["image"],
                json_response["generation-time"],
                json_response["Warning!"],
            )


def options():
    """
    Get available options
    """
    response = get("https://shard-ai.xyz/v1/sd1x/models")
    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code}")
    response_json = response.json()
    return ImageOptions(
        response_json["models"],
        response_json["ratios"],
        response_json["samplers"],
        response_json["upscale"],
    )


async def options_async():
    """
    Get available options
    """
    async with ClientSession() as session:
        async with session.get("https://shard-ai.xyz/v1/sd1x/models") as response:
            json_response = await response.json()
            if response.status != 200:
                raise ValueError(f"Error: {response.status}")
            return ImageOptions(
                json_response["models"],
                json_response["ratios"],
                json_response["samplers"],
                json_response["upscale"],
            )
