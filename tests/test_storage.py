import pytest
from io import BytesIO
import os
from config import Config

def test_upload_file(client):
    data = {
        'file': (BytesIO(b'test file content'), 'test.txt')
    }
    response = client.post('/storage/upload', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert 'filename' in json_data['data']

def test_upload_no_file(client):
    response = client.post('/storage/upload')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['status'] == 'error'

def test_download_file(client, app):
    # First upload a file
    test_content = b'test file content'
    data = {
        'file': (BytesIO(test_content), 'test.txt')
    }
    upload_response = client.post('/storage/upload', data=data)
    filename = upload_response.get_json()['data']['filename']
    
    # Then try to download it
    response = client.get(f'/storage/download/{filename}')
    assert response.status_code == 200
    assert response.data == test_content

def test_download_nonexistent_file(client):
    response = client.get('/storage/download/nonexistent.txt')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['status'] == 'error'