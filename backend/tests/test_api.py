"""
Endpoint: /api/result
Objective: Check if fetchable
"""


def test_get_result_list(client):
    response = client.get("/api/result/")
    assert response.status_code == 200


# """
# Endpoint: /api/result
# Objective: Check if postable
# """
# def test_post_result(client):
#     response = client.post("/api/result/list")
#     assert response.status_code == 200
