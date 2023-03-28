import os
import openai

PROGRAMMING_LANGUAGES = ["Python", "Go", "Java", "TypeScript"]
PROGRAMMING_CONCEPTS = ["Variables", "Functions", "Object Oriented Programming", "Polymorphism", "Control Structures"]
openai.api_key = os.getenv("OPENAI_SECRET_KEY")


def generate_tutorial(concept: str, language: str):

    prompt = f"Explain {concept} with a single example in {language}"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content