import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("you must supply a prompt!")
        sys.exit(1)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=sys.argv[1],
    )

    print(response.text)
    print(f"""
    Prompt tokens: {response.usage_metadata.prompt_token_count}
    Response tokens: {response.usage_metadata.candidates_token_count}
    """)


if __name__ == "__main__":
    main()
