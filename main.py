from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hi Gemini"
)
from voice import run_assistant


if __name__ == "__main__":
    run_assistant()

