import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
	    return client

def test_index(client):
    response = client.get('/')
    assert b'Farm animals' in response.data

def test_cow(client):
    response = client.get('animal/cow')
    assert b'MOoooOo!' in response.data

def test_pig(client):
    response = client.get('animal/pig')
    assert b'Oink oink!' in response.data

def test_sheep(client):
    response = client.get('animal/sheep')
    assert b'Baaaah!' in response.data

