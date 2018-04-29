import ridTests

def test_answer():
    myConn = ridTests.Connection()

    username='myName'
    key='myKey'

    myConn.login(username,key)
    assert True==True
