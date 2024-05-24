def test_login_page(client):
    response = client.get("/")
    assert b"<h1>Entre com seu log-in</h1>" in response.data