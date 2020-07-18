import mw_api_client as mw
import keyboard  # using module keyboard
import time

username = "\n"
password = "\n"
wp = mw.Wiki("https://en.scratch-wiki.info/w/api.php", "PyUserScript version 0.2.1")
print ("Please write your username, then press enter")
input (username)
print ("Password?")
input (password)
wp.login(username, password)

invitesender = wp.page("Scratch Wiki:Discussion_Invitation/List")
# Get the page
contents = invitesender.read()
print (contents)
time.sleep (3)
print ("Are you sure? It will send the invitations in next step? (y/n)")
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('y'):  # if key 'q' is pressed 
            print("Write only the page's interwiki link, don't add [[]]")
            input (link)
    except keyboard.is_pressed('n'):
        break
    break
# Change
contents += "\n Work in progress, a new user gadget."
summary = "Made a test edit with [[User:Ahmetlii/UserScript|UserScript]]"

# Submit
invitesender.edit(contents, summary)
