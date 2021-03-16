def test_get_tag_list(client):
    """
    Endpoint: /api/tags
    Objective: Check if fetchable
    """
    response = client.get("/api/tags/")
    assert response.status_code == 200
