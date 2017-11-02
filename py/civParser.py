from lxml import html
from bs4 import BeautifulSoup
import requests

def getEnv():
	return {'site': 'http://www.civstats.com/viewgame.php?gameid=2971'}
	


def getsite(site):
	page = requests.get(site)
	tree = html.fromstring(page.content)	
	soup = BeautifulSoup(page.content, 'html.parser')
	return tree

def gettables(soup):
	return soup.find_all('table')

#def splitHref(href):
#	d = 

def getPlayerSummary(playerSum):
	numCols = int(playerSum.select('tr td[colspan]')[0]['colspan'])
	d = {}
	for row in playerSum.findAll('tr'):
		li = []
		print(row)
		for item in row.findAll('td'):
			li.append(item.contents)
		d[li[1].contents] = {'turnTaken': True if li[0].contents == '*' else False,
				'playerPage':li[1]['href'],
				'leader':li[2].contents,
				'nation':li[3].contents,
				'score':li[4].contents,
				'status':li[5].contents}
	return li
##		print '======================'
#		print row
#		print '======================'
#		first_column = row.findAll('td')[0]#.contents
##		sec_col = row.findAll('td')[1].contents
##		third_column = row.findAll('td')[2].contents
#		print first_column#, sec_col, third_column
#
if __name__=='__main__':
	site = 'http://www.civstats.com/viewgame.php?gameid=2971'


