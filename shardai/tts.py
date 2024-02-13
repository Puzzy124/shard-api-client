from requests import get
from aiohttp import ClientSession
from .objects import TTSResponse, Voice


def completions(prompt: str, voice: str = "Rachel", api_key: str = None):
    """
    Text to speech function
    """
    if api_key is None:
        raise ValueError("API key is required for this function")
    if prompt is None:
        raise ValueError("Prompt is required for this function")
    headers = {"api-key": f"{api_key}"}
    payload = {"prompt": prompt, "voice": voice}
    response = get(
        "https://shard-ai.xyz/v1/tts/completions", json=payload, headers=headers
    )
    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code}")
    response_json = response.json()
    return TTSResponse(response_json["audio"])


async def completions_async(prompt: str, voice: str = "Rachel", api_key: str = None):
    """
    Text to speech function
    """
    if api_key is None:
        raise ValueError("API key is required for this function")
    if prompt is None:
        raise ValueError("Prompt is required for this function")

    headers = {"api-key": f"{api_key}"}
    payload = {"prompt": prompt, "voice": voice}
    async with ClientSession() as session:
        async with session.post(
            "https://shard-ai.xyz/v1/tts/completions", json=payload, headers=headers
        ) as response:
            json_response = await response.json()
            if response.status != 200:
                raise ValueError(f"Error: {response.status}")
            return TTSResponse(json_response["audio"])


def voices():
    """
    Get available voices
    """
    response = get("https://shard-ai.xyz/v1/tts/voices")
    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code}")
    response_json = response.json()
    return [
        Voice(voice["name"], voice["labels"], voice["preview_url"])
        for voice in response_json["voices"]
    ]


async def voices_async():
    """
    Get available voices
    """
    async with ClientSession() as session:
        async with session.get("https://shard-ai.xyz/v1/tts/voices") as response:
            json_response = await response.json()
            if response.status != 200:
                raise ValueError(f"Error: {response.status}")
            return [
                Voice(voice["name"], voice["labels"], voice["preview_url"])
                for voice in json_response["voices"]
            ]
