def hello_world(name):
    return f"Hello, {name}!"

def test_hello_world():
    assert hello_world("World") == "Hello, World!"
    assert hello_world("Alice") == "Hello, Alice!"
    assert hello_world("") == "Hello, !"