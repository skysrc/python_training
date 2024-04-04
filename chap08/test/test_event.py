from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_event():
    response = client.get("/event")
    assert response.status_code == 200

def test_about():
    response = client.get("/about")
    assert response.json() == {"detail" : "Not Found"}

def test_get_one_event():
    #get the token
    headers2 = {"Content-Type": "application/x-www-form-urlencoded"}
    body = {"username": "sky@gmail.com", "password": "gooderneh"}
    response2 = client.post("/user/signin", data=body, headers=headers2)
    data2 = response2.json()
    access_token = data2.get("access_token")
    print(data2)
    # access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2t5QGdtYWlsLmNvbSIsImV4cGlyZSI6MTcxMjIwMDU3My4xOTUyMzN9.BYebFusfZ_lcdCfVvjL6JdRNz981HzCaIpq_48LOlDo'
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    response = client.get("/event/1", headers=headers)
    assert response.status_code == 200
    data = response.json() # convert the returned JSON into dict / list
    assert data.get("title") == "string"