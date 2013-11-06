import re
from collections import Counter

def count(sana):
	try:
		with open('chatlog.log', 'rb') as chatlog:
			chatlog = chatlog.read().decode('latin-1')
	except IOError:
		return 'ei voi lukea chatlogia'
	nimet = re.findall('(?:conf@conference\.eddykaykay\.pw/)(.*?)(?:/.*?:\s)(?:.*?)(?:'+sana+')', chatlog)
	wc = Counter(nimet)
	return str(wc).lstrip('Counter')
