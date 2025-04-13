# A2A Crew Test

Test implementation of A2A protocol with CrewAI

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file with your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your_key_here" > .env
   ```

## Usage

Run the simple crew example:
```bash
python src/simple_crew.py
```

Run tests:
```bash
pytest tests/
```

## Project Structure

- `src/`: Source code
- `tests/`: Test files
- `requirements.txt`: Project dependencies
