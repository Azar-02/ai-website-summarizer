
import os
from openai import OpenAI
from dotenv import load_dotenv

from scraper import fetch_website_contents

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = """
You are an AI website summarizer.
Summarize the main content clearly and accurately.
Ignore navigation menus and unrelated website elements.
Respond in Markdown with a short summary and key points.
"""


def summarize(url):
    website = fetch_website_contents(url)

    response = client.chat.completions.create(
        # Replace with a model available in your Groq account
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"Summarize this website:\n\n{website}",
            },
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    summary = summarize("https://example.com")
    print(summary)
