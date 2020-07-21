import mw_api_client as mw
import keyboard  # using module keyboard
import re
import mwparserfromhell
import time
wp = mw.Wiki("https://en.scratch-wiki.info/w/api.php", "PyUserScript version 0.4.1")
username = input('Please write your username, then press enter\n')
password = input('Password?\n')
wp.clientlogin(username, password)
invitesender = wp.page("Scratch_Wiki:Discussion_Invitation/List")
user = 'User talk:'
wikicode=mwparserfromhell.parse(invitesender)
repeat = 0
item=wikicode.filter_templates(recursive=False)[0]
for template in wikicode.filter_templates():
     if template.name.matches("/item"):
          users = str(template.get(1).value)     
          lister = [user+users]
          link = input('Write the page exactly that you want to invite')
          allpos = len(lister)
          for x in lister:
               listread = wp.page(x)
               contents = listread.read()
               contents += '\n==Discussion Invitation==\n{{Discussion Invitation|'+link+'}}\nThis invitation sent by [[User:Ahmetlii/PyUserScript|PyUserScript]]. If you do not want to take invitations automatically, please contact with the [[User talk:'+username+'|'+username+']] for invitations or the [[User talk:Ahmetlii|programmer]] for errors.'
               summary = "Sent an invitation with [[User:Ahmetlii/PyUserScript|PyUserScript]]"
               listread.edit(contents, summary)
               repeat=repeat+1
               print("Invitations sent by autoscript ("+repeat+"-"+allpos+") Close the terminal when all of them are sent.")
