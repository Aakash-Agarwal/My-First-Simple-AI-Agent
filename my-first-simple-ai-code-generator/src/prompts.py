def developer_prompt(language, problem_description):
    return f"Write {language} code to solve the following problem:\n\n\"{problem_description}\""

def reviewer_prompt(code, problem_description):
    return f"Review the following code. Problem Statement:\n\"{problem_description}\"\n\nCode:\n{code}\n\nOutput the rating only, without any additional text."

def comments_prompt(problem_description, code):
    return f"Provide detailed review comments. Problem Statement:\n\"{problem_description}\"\n\nCode:\n{code}"