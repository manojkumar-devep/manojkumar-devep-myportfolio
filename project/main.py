from pathlib import Path

import pandas as pd

from text_processor import analyze_text
from image_processor import analyze_image
from speech_processor import speech_to_text


def process_messages(messages_path: Path | None = None) -> None:
    """Process the non-empty text, image, and voice fields in a CSV file."""
    if messages_path is None:
        messages_path = Path(__file__).resolve().parent / "data" / "messages.csv"

    if not messages_path.is_file():
        raise FileNotFoundError(f"Messages CSV not found: {messages_path}")

    messages = pd.read_csv(messages_path)

    for _, row in messages.iterrows():
        text = row.get("text", "")
        image = row.get("image", "")
        voice = row.get("voice", "")

        if pd.notna(text) and str(text).strip():
            analyze_text(text)
        if pd.notna(image) and str(image).strip():
            analyze_image(image)
        if pd.notna(voice) and str(voice).strip():
            speech_to_text(voice)


if __name__ == "__main__":
    process_messages()
