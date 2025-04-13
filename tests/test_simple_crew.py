from src.simple_crew import create_researcher, create_writer

def test_create_researcher():
    researcher = create_researcher()
    assert researcher.role == 'Researcher'
    assert researcher.allow_delegation == False

def test_create_writer():
    writer = create_writer()
    assert writer.role == 'Writer'
    assert writer.allow_delegation == False
