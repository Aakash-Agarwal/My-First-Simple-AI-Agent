from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

import os

# Load environment variables from a .env file
load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key  = os.getenv("OPENAI_API_KEY")
)

def ask_me_anything():
    """
    This function takes a query string as input and returns a response string.
    It uses the ChatOpenAI model to generate the response.
    """
    query = input("Enter your query: ")
    print("Analysing your query...", "\n")
    
    # Generate a response using the model
    response = llm.invoke(query)

    # Wait for the response to be generated
    while response is None:
        pass  # Wait for the response

    print(response.content)

print("Press 0 to exit and 1 to continue")
while True:
    choice = input("Enter your choice: ")
    if choice == "0":
        print("Exiting...")
        break
    elif choice == "1":
        ask_me_anything()
    else:
        print("Invalid choice. Please enter 0 or 1.")
# This code is a simple command-line interface that allows users to ask questions and receive answers using the OpenAI API.