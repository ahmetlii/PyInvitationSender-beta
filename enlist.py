import mw_api_client as mw
import keyboard  # using module keyboard
import re
import time
import mwparserfromhell
wp = mw.Wiki("https://en.scratch-wiki.info/w/api.php", "PyUserScript version 0.2.1")
invitesender = wp.page("Scratch_Wiki:Discussion_Invitation/List")
user="User talk:"
wikicode=mwparserfromhell.parse(invitesender)
item=wikicode.filter_templates(recursive=False)[0]
for template in wikicode.filter_templates():
     if template.name.matches("/item"):
          users=str(template.get(1).value)         
          lister=user,users
          endarg=wp.page(lister)
          contents=endarg.read()
          print(contents)
