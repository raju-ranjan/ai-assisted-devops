import google.generativeai as genai
import os

# Set your API key here
os.environ["GOOGLE_API_KEY"] = "AIzaSyCDqgj6QDb2wjBAnu6nD9_zjg9P5KPN1aQ"

# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


from google.generativeai import list_models
models = list_models()
for model in models:
    print(model.name)

model = genai.GenerativeModel('gemini-2.5-pro')

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. Just share the dockerfile without any explanation between two lines to make copying dockerfile easy.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)

