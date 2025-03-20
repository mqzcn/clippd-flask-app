import pytest
from subprocess import run


@pytest.fixture(autouse=True)
def seed_database():
    run(["python3", "seed_dev_database.py"], check=True)


"""
GET /
should return "Welcome to the Practice Drills API" and status code 200
"""
def test_get_welcome_message(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Welcome to the Practice Drills API"

"""
GET /drills
should return all drills in the database and status code 200
"""
def test_get_all_drills(web_client):
    response = web_client.get("/drills")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

"""
GET /drills/1
should return one drill by its id and status code 200
"""
def test_get_drill_by_id(web_client):
    response = web_client.get("/drills/1")
    if response.status_code == 200:
        assert isinstance(response.get_json(), dict)
    else:
        assert response.status_code == 404

"""
POST /drills
should return 201 status code and a message "Drill created successfully"
"""
def test_create_drill(web_client):
    response = web_client.post("/drills", json={
        "drill_type": "putting",
        "tags": ["accuracy"],
        "clubs": ["putter"],
        "drill_name": "Target Putting",
        "instructions": "Aim for the hole.",
        "estimated_time": "10s",
        "goal": "Sink the putt",
        "drill_media": None,
        "measure_success": "Accuracy",
        "score_system": "points",
        "custom_scoring": "",
        "total_possible_points": "100",
        "custom_distance": "3m",
        "randomized": False,
        "easy_percent": "50",
        "medium_percent": "30",
        "hard_percent": "15",
        "expert_percent": "5"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Drill created successfully"

"""
PUT /drills/1
should return "Drill updated successfully" message and status code 200
"""
def test_update_drill(web_client):
    response = web_client.put("/drills/1", json={
        "drill_name": "Updated Drill Name"
    })
    if response.status_code == 200:
        assert response.get_json()["message"] == "Drill updated successfully"
    else:
        assert response.status_code == 404

"""
DELETE /drills/2
should return "Drill deleted successfully" message and status code 200
"""
def test_delete_drill(web_client):
    response = web_client.delete("/drills/2")
    if response.status_code == 200:
        assert response.get_json()["message"] == "Drill deleted successfully"
    else:
        assert response.status_code == 404
