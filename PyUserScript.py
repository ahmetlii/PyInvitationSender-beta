import mw_api_client as mw
import keyboard  # using module keyboard
import re
import mwparserfromhell
import time
username = "\n"
password = "\n"
wp = mw.Wiki("https://en.scratch-wiki.info/w/api.php", "PyUserScript version 0.4.1")
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
          users=str(template.get(1).value)     
          lister=[user+users]
          listread=wp.page(lister)
          contents=listread.read()
     break
print ("Are you sure? It will send the invitations in next step. Please check limitations about invitations, this tool has not liability and guarantee on edits.(y for if you are sure)")
keyboard.wait("y")
print("Write the page exactly that you want to invite")
input(link)      
contents += "==Discussion Invitation== \n {{Discussion Invitation|"+link+"}} \n If you don't want to take invitations automatically, please contact with the [[User talk:"+username+"|"username"]] for invitations or the [[User:Ahmetlii|programmer]] for errors."
summary = "Sent an invitation with [[User:Ahmetlii/PyUserScript|PyUserScript]]"
print("Invitations sent by autoscript. Please exit from the terminal.")
time.sleep(3)
