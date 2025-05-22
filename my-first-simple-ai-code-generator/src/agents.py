from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

class DeveloperAgent:
    def __init__(self):
        self.agent = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate_code(self, prompt):
        response = self.agent.invoke(prompt)
        return response.content if hasattr(response, "content") else response

class ReviewerAgent:
    def __init__(self):
        self.agent = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def review_code(self, prompt):
        response = self.agent.invoke(prompt)
        return response.content if hasattr(response, "content") else response

    def get_comments(self, prompt):
        comments_response = self.agent.invoke(prompt)
        return comments_response.content.split("\n") if hasattr(comments_response, "content") else comments_response.split("\n")