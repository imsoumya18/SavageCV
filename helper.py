from openai import OpenAI
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Get the API key from the .env file

def get_openai_response(profile, lang=""):
    try:
        prompt = f"""
        You are a professional roaster. Here is the contents of my CV:
        {profile}
        
        Based on the above CV, roast the profile aggressively within 150 words.
        Use markdown format only. Do bold, italics, headings, subheadings, bullets, etc formatting wherever needed.
        Add emojis also to make it engaging.
        """

        if lang != "":
            prompt += f"""
            Use puns from {lang} movies, songs, books, literature, news, politics, idioms or any cultural or sarcastic contexts at appropriate positions.
            You can add the English translation in braces though.
"""

        response = client.chat.completions.create(model="gpt-4",
                                                  messages=[{"role": "user", "content": prompt}],
                                                  temperature=0.4)
        # Extract the content of the response
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


def read_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"An error occurred: {e}"
