def login():
    return "<h1>Faça seu log-in no sistema</h1>"

def test_login_page():
    assert login() == "<h1>Faça seu log-in no sistema</h1>", "Deve ter retornar um html" 

test_login_page()
