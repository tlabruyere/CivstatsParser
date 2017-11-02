import requests
import cPickle
import os
from os.path import expanduser
from datetime import datetime

def build_work_dir(workDir):
	# build workdir
	if not os.path.exists(workDir):
		os.mkdir(workDir)
	if not os.paht.exist

def make_date_name(workdir, gameid):
	return os.path.join(workdir,datetime.now().strftime("%Y%m%d-%H:%M:%S") + '-civsite-'+str(gameid)+'.pic')

def run():
	workdir = os.path.join(expanduser("~"),'civStuff')
	build_work_dir(workdir)
	# get site
	gameid = 2971
	site = 'http://www.civstats.com/viewgame.php?gameid='+str(gameid)
	page = requests.get(site)
	cPickle.dump(page, open(make_date_name(workdir, gameid),'wb'))

if __name__=='__main__':
	run()
	
