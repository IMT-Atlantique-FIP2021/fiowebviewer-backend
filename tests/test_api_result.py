def test_get_result_list(client):
    """
    Endpoint: /api/result
    Objective: Check if fetchable
    """
    response = client.get("/api/result/")
    assert response.status_code == 200


# def test_post_result_list(client):
#     """
#     Endpoint: /api/result
#     Objective: Check if postable
#     """
#     response = client.post("/api/result/")
#     assert response.status_code == 200
