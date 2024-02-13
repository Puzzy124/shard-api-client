from requests import get
from aiohttp import ClientSession
from .objects import ChatResponse


def completions(prompt: str, model: str, api_key: str = None):
    """
    Chat function
    """
    if api_key is None:
        raise ValueError("API key is required for this function")
    if prompt is None:
        raise ValueError("Prompt is required for this function")
    headers = {"api-key": api_key, "Content-Type": "application/json"}
    payload = {"messages": [{"role": "user", "content": prompt}], "model": model}
    response = get(
        "https://shard-ai.xyz/v1/chat/completions", json=payload, headers=headers
    )
    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code}")
    response_json = response.json()
    return ChatResponse(
        response_json["id"],
        response_json["object"],
        response_json["created"],
        response_json["model"],
        response_json["usage"],
        response_json["choices"],
    )


async def completions_async(prompt: str, model: str, api_key: str = None):
    """
    Chat function
    """
    if api_key is None:
        raise ValueError("API key is required for this function")
    if prompt is None:
        raise ValueError("Prompt is required for this function")

    headers = {"api-key": api_key, "Content-Type": "application/json"}
    payload = {"messages": [{"role": "user", "content": prompt}], "model": model}
    async with ClientSession() as session:
        async with session.post(
            "https://shard-ai.xyz/v1/chat/completions", json=payload, headers=headers
        ) as response:
            json_response = await response.json()
            if response.status != 200:
                raise ValueError(f"Error: {response.status}")
            print(json_response)
            return ChatResponse(
                json_response["id"],
                json_response["object"],
                json_response["created"],
                json_response["model"],
                json_response["usage"],
                json_response["choices"],
            )


def models():
    """
    Get available models
    """
    response = get("https://shard-ai.xyz/v1/chat/models")
    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code}")
    response_json = response.json()
    return response_json["models"]


async def models_async():
    """
    Get available models
    """
    async with ClientSession() as session:
        async with session.get("https://shard-ai.xyz/v1/chat/models") as response:
            json_response = await response.json()
            if response.status != 200:
                raise ValueError(f"Error: {response.status}")
            return json_response["models"]
