import mw_api_client as mw

username = "\n"
password = "\n"
wp = mw.Wiki("https://en.scratch-wiki.info/w/api.php", "PyUserScript version 0.2.1")

print ("Please write your username, then press enter")
input (username)
print ("Password?")
input (password)
wp.login(username, password)

sandbox = wp.page("User:Ahmetlii/Sandbox")
# Get the page
contents = sandbox.read()

# Change
contents += "\n Work in progress, a new user gadget."
summary = "Made a test edit with [[User:Ahmetlii/UserScript|UserScript]]"
