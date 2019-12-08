import json
from markdown2 import markdown

config = open("config.json", "r")	

configurated = json.load(config)	

sitefile = open("pages/index.html", "r")	

data = sitefile.read()	
data = data.replace("///site", configurated["site"])	
sitefile = open("pages/index.html", "w")	
sitefile.write(data)	
sitefile.close()

sitefile = open("config/main.md", r)

d = sitefile.read()
d = markdown(d)
sitefile.close()
sitefile = open("/pages/index.html", w+)
data = sitefile.read()
data = data.replace("{{body}}",d)
data = data.replace("{{site}}",configurated["site"])
data = data.replace("{{issue-number}}",configurated["issue-number"])
sitefile.write(data)
sitefile.close()
