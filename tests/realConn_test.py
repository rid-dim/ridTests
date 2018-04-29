import ridTests

def test_noConnectionPossible():
    myTst=ridTests.Connection()
    myTst.login('halloe','nanu')

    assert myTst.lastError == -2000

def test_accountDoesntExist():
    myTst=ridTests.Connection()
    myTst.login('halloe','nanu')

    assert myTst.lastError == -101


