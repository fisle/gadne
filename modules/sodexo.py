import urllib.request,datetime,json,sys

triggers = ['!ict']

def run(msg):

    arguments = msg['body'].split()[1:]

    days = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su']
    date = datetime.datetime.now()
    koko = False

    try:
        delta = int(arguments[0])
        date += datetime.timedelta(days=delta)
        paiva = date.weekday()
    except:
        if len(arguments) != 0:
            if arguments[0] in days:
                paiva = days.index(arguments[0])
                date += datetime.timedelta(days=paiva-date.weekday())
            if arguments[0] == 'koko':
                koko = True
                paiva = date.weekday()
        else:
            paiva = date.weekday()

    try:
        ret = ''
        while 1:
            ruokalista = json.loads(urllib.request.urlopen(
                    'http://www.sodexo.fi/ruokalistat/output/daily_json/54/'
                    '{0}/{1}/{2}/fi'.format(date.year, date.month, date.day)
                ).read().decode())
            ret += days[date.weekday()] + ': '
            for ruoka in ruokalista['courses']:
                ret += '| {0}{1} |'.format(
                    ruoka['price'].split('/')[0], ruoka['title_fi'])
            if koko == False:
                break
            paiva += 1
            if paiva > 4:
                break
            ret += '\n'
            date += datetime.timedelta(days=1)
        if 'riisi' in ret.lower():
            ret += ' "Taas riisiä" :grage:'
        else:
            ret += ' ja riisiä'
        return ret
    except:
        return 'jotain hajos'
