import mw_api_client as mw
import keyboard  # using module keyboard
import re
import time
import mwparserfromhell
username = "\n"
password = "\n"
wp = mw.Wiki("https://en.scratch-wiki.info/w/api.php", "PyUserScript version 0.2.1")
print ("Please write your username, then press enter")
input (username)
print ("Password?")
input (password)
wp.clientlogin(username, password)
invitesender = wp.page("Scratch_Wiki:Discussion_Invitation/List")
user='User talk:'
wikicode=mwparserfromhell.parse(invitesender)
item=wikicode.filter_templates(recursive=False)[0]
for template in wikicode.filter_templates():
     if template.name.matches("/item"):
          users=template.get(1).value         
          lister=user,users
          endarg=wp.page(lister)
          contents=endarg.read()
          print(contents)

# Get the page
contents = lastlis.read()
print (contents)
time.sleep (3)
print ("Are you sure? It will send the invitations in next step? (y/n)")
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('y'):  # if key 'q' is pressed
            
            contents += "==Discussion Invitation== \n {{Discussion Invitation|"+link+"}}"
    except keyboard.is_pressed('n'):
        break
    break
# Change
contents += "\n Work in progress, a new user gadget."
summary = "Made a test edit with [[User:Ahmetlii/UserScript|UserScript]] If it has an malfunctioning, please contact with the user."

# Submit
invitesender.edit(contents, summary)
#List pages in category:

#for page in wp.category("Redirects").categorymembers():
    #print(page.title)

openuserpage = wp.template("Open userpage")

# Pages that transclude stub, main namespace only
target_pages = list(openuserpage.transclusions(namespace=0))

# Sort by title because it's prettier that way
target_pages.sort(key=lambda p: "User:Ahmetlii/")

for page in target_pages:
    page.replace(" ", "{{openuserpage}}")
#Patrol all recent changes in the Help namespace:

#rcs = wp.recentchanges(rcnamespace=12)

#for rc in rcs:
    #rc.patrol()
