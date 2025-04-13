import pytest
from src.simple_crew import create_researcher, create_writer, create_tasks

def test_agent_creation():
    """Test that agents are created with correct attributes"""
    researcher = create_researcher()
    writer = create_writer()
    
    assert researcher.role == 'Researcher'
    assert researcher.goal == 'Analyze and gather information'
    assert not researcher.allow_delegation
    
    assert writer.role == 'Writer'
    assert writer.goal == 'Write clear and engaging content'
    assert not writer.allow_delegation

def test_task_creation():
    """Test that tasks are created with correct descriptions"""
    researcher = create_researcher()
    writer = create_writer()
    tasks = create_tasks(researcher, writer)
    
    assert len(tasks) == 2
    assert tasks[0].description == 'Research the benefits of AI in software development'
    assert tasks[1].description == 'Write a summary of the research findings'

print("\nTo use this code with OpenAI:")
print("1. Get a valid OpenAI API key from https://platform.openai.com/account/api-keys")
print("2. Update the .env file with your key:")
print("   OPENAI_API_KEY=your-actual-api-key")
print("\nRepository structure:")
print("~/A2A-crew-test/")
print("├── .env                    # API key configuration")
print("├── src/")
print("│   └── simple_crew.py      # Main CrewAI implementation")
print("├── tests/")
print("│   ├── test_simple_crew.py # Basic tests")
print("│   └── test_crew_structure.py # Structure tests")
print("└── requirements.txt        # Project dependencies")
print("\nTo run the actual CrewAI example:")
print("1. Set up your OpenAI API key in .env")
print("2. Activate the virtual environment: source .venv/bin/activate")
print("3. Run: python src/simple_crew.py")
