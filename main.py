import json
from markdown2 import markdown

config = open("config.json", "r")	

configurated = json.load(config)	

sitefile = open("templates/stuff.html", "r")	

data = sitefile.read()	
data = data.replace("///site", configurated["site"])	
sitefile = open("pages/index.html", "w")	
sitefile.write(data)	
sitefile.close()
