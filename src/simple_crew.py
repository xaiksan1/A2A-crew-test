import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def get_openai_api_key():
    return os.getenv('OPENAI_API_KEY', 'dummy-key')

# Create LLM instance
llm = ChatOpenAI(
    openai_api_key=get_openai_api_key(),
    model="gpt-3.5-turbo",  # Using a more accessible model
    temperature=0.7
)

# Create a basic researcher agent
def create_researcher():
    return Agent(
        role='Researcher',
        goal='Analyze and gather information',
        backstory='Expert at analyzing and gathering accurate information',
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

# Create a basic writer agent
def create_writer():
    return Agent(
        role='Writer',
        goal='Write clear and engaging content',
        backstory='Expert at writing clear and engaging content',
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

# Create tasks
def create_tasks(researcher, writer):
    research_task = Task(
        description='Research the benefits of AI in software development',
        agent=researcher
    )
    
    writing_task = Task(
        description='Write a summary of the research findings',
        agent=writer
    )
    
    return [research_task, writing_task]

def main():
    # Initialize agents
    researcher = create_researcher()
    writer = create_writer()
    
    # Create tasks
    tasks = create_tasks(researcher, writer)
    
    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=tasks,
        verbose=True
    )
    
    # Start the crew
    result = crew.kickoff()
    
    return result

if __name__ == "__main__":
    print(main())
