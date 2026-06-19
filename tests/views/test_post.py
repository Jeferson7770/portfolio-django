import pytest 

@pytest.mark.django_db
def test_post_view(client):
    
    url = '/home/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Hello Word'