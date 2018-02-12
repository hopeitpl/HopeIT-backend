import falcon


def test_ping(client):
    res = client.simulate_get(f'/_ping')
    assert res.status == falcon.HTTP_200
    assert res.json['results'] == 'pong'
