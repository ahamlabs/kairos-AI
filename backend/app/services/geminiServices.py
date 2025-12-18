from prompts import GEN_SYLLABUS
from google import genai
from dotenv import load_dotenv
import os
import random
import uuid
import re

load_dotenv()


class GeminiService:
    def __init__(self, user_goal_context: str):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = "gemini-2.5-flash-lite-preview-09-2025"
        self.USER_GOAL_CONTEXT = user_goal_context
        self.USER_ID = str(uuid.uuid4())

    def user_id(self):
        return self.USER_ID

    def generate_content(self):
        response = self.client.models.generate_content(model=self.model, contents=GEN_SYLLABUS.format(USER_GOAL_CONTEXT=self.USER_GOAL_CONTEXT, USER_ID=self.USER_ID))
        return response.text

    def search_queries(self):
        response = self.generate_content()
        os.makedirs("./data", exist_ok=True)
        pattern: str = r'```json(.*?)```'
        match = re.search(pattern, response, re.DOTALL)
        # print(match.group(1))
        if match:
            os.makedirs(f"./data/{self.USER_ID}", exist_ok=True)
            with open(f"./data/{self.USER_ID}/syllabus.json", "w") as f:
                f.write(match.group(1))
        else:
            raise Exception("No match found")

    def run(self):
        self.search_queries()   

if __name__ == "__main__":
    user_goal_context: str = input("Enter the user goal context: ")
    gemini_service = GeminiService(user_goal_context)
    gemini_service.run()
