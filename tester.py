import mw_api_client as mw

username = "\n"
password = "\n"
wp = mw.Wiki("https://en.scratch-wiki.info/w/api.php", "PyUserScript version 0.2.1")
print ("Please write your username, then press enter")
input (username)
print ("Password?")
input (password)
wp.clientlogin(username, password)
sandbox = wp.page("User:Ahmetlii/Sandbox2")
contents = sandbox.read()
print(contents)
