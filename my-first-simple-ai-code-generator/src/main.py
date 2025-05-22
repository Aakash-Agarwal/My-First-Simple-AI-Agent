from dotenv import load_dotenv
import os
from agents import DeveloperAgent, ReviewerAgent
from prompts import developer_prompt as create_developer_prompt, reviewer_prompt as create_reviewer_prompt, comments_prompt
from utils import get_user_prompt

load_dotenv()

developer = DeveloperAgent()
reviewer = ReviewerAgent()
rating_required = 9

def main():
    language, problem_description = get_user_prompt()
    generate_code_with_developer(language, problem_description)

def generate_code_with_developer(language, problem_description):
    prompt = create_developer_prompt(language, problem_description)
    generated_code = developer.generate_code(prompt)
    print("Generated Code:\n")
    print(generated_code)
    review_code_with_reviewer(language, problem_description, generated_code)

def review_code_with_reviewer(language, problem_description, code):
    prompt = create_reviewer_prompt(code, problem_description)
    rating = int(reviewer.review_code(prompt).strip())
    
    if rating < rating_required:
        prompt = comments_prompt(problem_description, code)
        comments = reviewer.get_comments(prompt)
        print(f"Rating: {rating}/10\nComments:\n{comments}")
        regenerate_code(comments, code, language)
    else:
        print(f"Rating: {rating}/10")

def regenerate_code(comments, code, language):
    generate_code_with_developer(language, code.join("\n\nReviewer Comments:\n").join(comments))

if __name__ == "__main__":
    main()