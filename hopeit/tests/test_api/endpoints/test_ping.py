import falcon


def test_ping(client):
    res = client.simulate_get(f'/_ping')
    # Should give HTTP 401, no auth token in header
    assert res.status == falcon.HTTP_401
