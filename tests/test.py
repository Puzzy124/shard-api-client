api_key = ""

from shardai import tts, chat, image


async def test_tts():
    prompt = "Hello, how are you?"
    voice = "Rachel"

    response = await tts.completions_async(prompt, voice, api_key)
    print(response.audio)


async def test_tts_voices():
    print(await tts.voices_async())


async def test_chat():
    print(await chat.models_async())
    prompt = "Hello, how are you?"
    response = await chat.completions_async(prompt, "llama_2_7b", api_key)
    print(response)
    print(response.choices)
    print(response.choices[0].message.content)
    print(response.choices[0].message.role)


async def test_image():
    prompt = "A beautiful sunset"
    response = await image.completions_async(prompt, api_key=api_key)
    print(response.image)
    print(response.generation_time)
    print(response.warning)


async def test_image_models():
    print(await image.options_async())


def main():
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_image_models())


if __name__ == "__main__":
    main()
