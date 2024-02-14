api_key = ""

from shardai import ShardClient

client = ShardClient(api_key)


async def test_tts():
    prompt = "Hello, how are you?"
    voice = "Rachel"

    response = await client.tts_async.completions(prompt, voice)
    print(response.audio)


async def test_tts_voices():
    print(await client.tts_async.voices())


async def test_chat():
    print(await client.chat_async.models())
    prompt = "Hello, how are you?"
    response = await client.chat_async.completions(prompt, "llama_2_7b")
    print(response)
    print(response.choices)
    print(response.choices[0].message.content)
    print(response.choices[0].message.role)


async def test_image():
    prompt = "A beautiful sunset"
    response = await client.image_async.completions(prompt)
    print(response.image)
    print(response.generation_time)
    print(response.warning)
    response = await client.image_async.turbo_completions(prompt)
    print(response.image)
    print(response.generation_time)
    print(response.warning)
    response = await client.image_async.sdxl_completions(prompt)
    print(response.image)
    print(response.generation_time)
    print(response.warning)
    await response.download_async("image.png")
    byte_response = await response.as_bytes_async()
    print(byte_response)


async def test_image_models():
    print(await client.image_async.sdxl_options())
    print(await client.image_async.options())


async def test_all():
    await test_tts()
    await test_tts_voices()
    await test_chat()
    await test_image()
    await test_image_models()


def main():
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_all())


if __name__ == "__main__":
    main()
