import pytest
import json

def test_generate_cv_success(client):
    data = {
        'name': 'John Doe',
        'skills': ['Python', 'Cloud Computing']
    }
    response = client.post('/ai/generate-cv',
                          data=json.dumps(data),
                          content_type='application/json')
    assert response.status_code == 200
    result = response.get_json()
    assert result['status'] == 'success'
    assert result['data']['name'] == 'John Doe'
    assert 'generated_sections' in result['data']

def test_generate_cv_missing_fields(client):
    data = {'name': 'John Doe'}  # Missing skills
    response = client.post('/ai/generate-cv',
                          data=json.dumps(data),
                          content_type='application/json')
    assert response.status_code == 400
    result = response.get_json()
    assert result['status'] == 'error'

def test_recommend_jobs_success(client):
    data = {
        'skills': ['Cloud Computing', 'DevOps']
    }
    response = client.post('/ai/recommend-jobs',
                          data=json.dumps(data),
                          content_type='application/json')
    assert response.status_code == 200
    result = response.get_json()
    assert result['status'] == 'success'
    assert 'recommendations' in result['data']

def test_recommend_jobs_invalid_skills(client):
    data = {
        'skills': 'not a list'  # Invalid skills format
    }
    response = client.post('/ai/recommend-jobs',
                          data=json.dumps(data),
                          content_type='application/json')
    assert response.status_code == 400
    result = response.get_json()
    assert result['status'] == 'error'