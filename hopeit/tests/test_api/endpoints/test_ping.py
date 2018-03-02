import falcon


def test_ping(client):
    res = client.simulate_get(f'/_ping')
    assert res.status == falcon.HTTP_401

    res = client.simulate_get(
        f'/_ping',
        headers={'Authorization': 'Basic YWRtaW46YWRtaW4='}
    )
    assert res.status == falcon.HTTP_200
    assert res.json['results'] == 'pong'
