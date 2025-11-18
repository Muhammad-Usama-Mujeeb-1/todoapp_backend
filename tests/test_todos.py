# Todo API endpoint tests
# TODO: Add tests for your todo endpoints
# Example structure:

# def test_get_todos(client):
#     """Test getting all todos"""
#     response = client.get("/api/v1/todos/")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#
# def test_create_todo(client, sample_todo):
#     """Test creating a todo"""
#     response = client.post("/api/v1/todos/", json=sample_todo)
#     assert response.status_code == 200
#     assert response.json()["name"] == sample_todo["name"]
#
# def test_get_todo_by_id(client):
#     """Test getting todo by ID"""
#     response = client.get("/api/v1/todos/1")
#     assert response.status_code == 200
#
# def test_update_todo(client):
#     """Test updating a todo"""
#     update_data = {"name": "Updated Todo"}
#     response = client.put("/api/v1/todos/1", json=update_data)
#     assert response.status_code == 200
#
# def test_delete_todo(client):
#     """Test deleting a todo"""
#     response = client.delete("/api/v1/todos/1")
#     assert response.status_code == 200