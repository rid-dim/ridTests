import ridTests, getpass

myConn = ridTests.Connection()

username=getpass.getpass()
key=getpass.getpass()

myConn.login(username,key)


