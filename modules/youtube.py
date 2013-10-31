import json
import urllib.request
import datetime
import re

def info(url):
	try:
		url = urllib.request.urlopen(url).geturl()
		match = re.search('(?:youtube\.com/|youtu\.be)(?:.*?v=|.*?embed/|.*?v/|/)(.{11})', url)
		videoid = match.group(1)
		jsondata = json.loads(urllib.request.urlopen('http://gdata.youtube.com/feeds/api/videos/'+videoid+'?v=2&alt=jsonc').read().decode())
		video = jsondata['data']
		kesto = ' ('+str(datetime.timedelta(seconds=video['duration']))+')'
		nippelitieto = ' / '.join(['Aihe: '+video['category'], '{:,}'.format(video['viewCount'])+' katselukertaa', 'likeratio: '+str(round(video['rating']*20, 2))+'%'])
		ret = 'Youtube: '
		ret += '['+video['uploader']+'] '+video['title']+kesto+' | '+nippelitieto
	except:
		return ''
	return ret