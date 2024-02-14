# ShardAI PKG

## Installation

```bash
pip install shardai
```

## Usage

```python
from shardai import ShardClient

client = ShardClient("your-api-key") # Replace with your API key

# Get all the available chat models
models = client.chat.models()

# Get the response from the chat model
response = client.chat.completions("Hello, how are you?", "llama_2_7b")

print(response.choices[0].message.content) # This will be a response from the model

# Get all the available image generation options

options = client.image.options()

# Get the response from the image generation model
response = client.image.completions("A picture of a cat")

print(response.image) # This will be an image as https://shard-ai.xyz/static/....png

response.image.download("cat.png") # This will download the image to the current directory

image_bytes = response.image.as_bytes() # This will return the image as bytes

# Get all the available tts voices
voices = client.tts.voices()

# Get the response from the tts model
response = client.tts.completions("Hello, how are you?")

print(response.audio) # This will be an audio encoded in base64
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

[ShardAI](https://shard-ai.xyz)
