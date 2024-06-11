from fastapi import status


def test_create_restaurant(test_client):
    restaurant_data = {
        "rating": 5,
        "name": "Test Restaurant",
        "site": "http://test.com",
        "email": "test@test.com",
        "phone": "123456789",
        "street": "123 Test St",
        "city": "Test City",
        "state": "Test State",
        "lat": 10.0,
        "lng": 20.0
    }


    response = test_client.post("/api/restaurants", json=restaurant_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == restaurant_data["name"]
    assert data["email"] == restaurant_data["email"]


def test_read_all_restaurants(test_client):
    response = test_client.get("/api/restaurants")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)

def test_read_restaurant_by_id(test_client):
    restaurant_data = {
        "rating": 5,
        "name": "Test Restaurant",
        "site": "http://test.com",
        "email": "test@test.com",
        "phone": "123456789",
        "street": "123 Test St",
        "city": "Test City",
        "state": "Test State",
        "lat": 10.0,
        "lng": 20.0
    }
    
    create_response = test_client.post("/api/restaurants", json=restaurant_data)
    restaurant_id = create_response.json()["id"]
    response = test_client.get(f"/api/restaurants/{restaurant_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == restaurant_id
    assert data["name"] == restaurant_data["name"]


def test_update_restaurant(test_client):
    restaurant_data = {
        "rating": 5,
        "name": "Test Restaurant",
        "site": "http://test.com",
        "email": "test@test.com",
        "phone": "123456789",
        "street": "123 Test St",
        "city": "Test City",
        "state": "Test State",
        "lat": 10.0,
        "lng": 20.0
    }
    create_response = test_client.post("/api/restaurants", json=restaurant_data)
    restaurant_id = create_response.json()["id"]
    updated_data = {
        "rating": 4,
        "name": "Updated Restaurant",
        "site": "http://updated.com",
        "email": "updated@test.com",
        "phone": "987654321",
        "street": "456 Updated St",
        "city": "Updated City",
        "state": "Updated State",
        "lat": 30.0,
        "lng": 40.0
    }
    response = test_client.put(f"/api/restaurants/{restaurant_id}", json=updated_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == updated_data["name"]
    assert data["email"] == updated_data["email"]


def test_delete_restaurant(test_client):
    restaurant_data = {
        "rating": 5,
        "name": "Test Restaurant",
        "site": "http://test.com",
        "email": "test@test.com",
        "phone": "123456789",
        "street": "123 Test St",
        "city": "Test City",
        "state": "Test State",
        "lat": 10.0,
        "lng": 20.0
    }
    create_response = test_client.post("/api/restaurants", json=restaurant_data)
    restaurant_id = create_response.json()["id"]
    response = test_client.delete(f"/api/restaurants/{restaurant_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["message"] == "Restaurant deleted successfully"
