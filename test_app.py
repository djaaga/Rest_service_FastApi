import requests


def test_get_salary_status_code():
    response = requests.get("http://localhost:8000/salary")
    assert response.status_code == 200
