import os
import time
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image


# Load environment variables
load_dotenv()

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN not found in .env file")


# Hugging Face client
client = InferenceClient(
    token=hf_token
)


# Output folder
OUTPUT_DIR = Path("generated_images")
OUTPUT_DIR.mkdir(exist_ok=True)


# Aspect ratio mapping
SIZE_MAP = {
    "1:1": (1024, 1024),
    "16:9": (1536, 1024),
    "9:16": (1024, 1536)
}


def generate_image(prompt, aspect_ratio="1:1", count=1):

    width, height = SIZE_MAP.get(
        aspect_ratio,
        (1024, 1024)
    )

    for image_number in range(count):

        print("\nGenerating image...")
        print(f"Prompt: {prompt}")
        print(f"Aspect Ratio: {aspect_ratio}")
        print(f"Resolution: {width}x{height}")
        print(f"Image Number: {image_number + 1}")

        for attempt in range(3):

            try:

                image = client.text_to_image(
                    prompt=prompt,
                    model="black-forest-labs/FLUX.1-schnell"
                )

                file_path = OUTPUT_DIR / (
                    f"generated_{int(time.time())}_"
                    f"{image_number + 1}.png"
                )

                image.save(file_path)

                # Verify image
                with Image.open(file_path) as img:
                    img.load()
                    print(f"\nSUCCESS: {file_path}")
                    print(f"Image size: {img.size}")

                break

            except Exception as error:

                print(
                    f"\nAttempt {attempt + 1} failed:"
                )
                print(error)

                if attempt < 2:
                    wait_time = 2 ** attempt
                    print(
                        f"Retrying in {wait_time} seconds..."
                    )
                    time.sleep(wait_time)

                else:
                    print(
                        "\nImage generation failed."
                    )


def main():

    print("=" * 60)
    print("MULTIMODAL IMAGE GENERATION STUDIO")
    print("=" * 60)

    prompt = input(
        "\nEnter your image prompt: "
    )

    print("\nChoose aspect ratio:")
    print("1. 1:1 Square")
    print("2. 16:9 Landscape")
    print("3. 9:16 Vertical")

    choice = input(
        "Enter choice (1/2/3): "
    )

    if choice == "2":
        aspect_ratio = "16:9"

    elif choice == "3":
        aspect_ratio = "9:16"

    else:
        aspect_ratio = "1:1"

    count_input = input(
        "\nHow many images? (1-3): "
    )

    try:
        count = int(count_input)

    except ValueError:
        count = 1

    count = max(1, min(count, 3))

    generate_image(
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        count=count
    )


if __name__ == "__main__":
    main()