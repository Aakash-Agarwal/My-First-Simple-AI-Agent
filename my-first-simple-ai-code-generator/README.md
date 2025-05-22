# My First Simple AI Code Generator

This project is a simple AI agent that generates and reviews code using AI models. It allows users to input a programming language and a problem description, generates code based on that input, and then reviews the generated code for quality and correctness.

## Project Structure

```
my-first-simple-ai-code-generator
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── agents.py
│   ├── prompts.py
│   └── utils.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-first-simple-ai-code-generator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file. You will need to include your API keys for the AI models.

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the prompts to input the programming language and problem description.

3. The application will generate code based on your input and provide a review of the generated code.

## Dependencies

- `langchain`
- `wikipedia`

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.