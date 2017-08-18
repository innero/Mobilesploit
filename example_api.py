import sys, os, socket, time

def auto_help(name,rank,description):
	stbl = "  " + name + " "*(13-len(name)+4) + rank + " "*(8-len(rank)+4) + description
	return stbl

def auto_targ(targetlist):
	print "Vulnrable Applications (%s)\n" %name
	print "  ID       Device"
	print "  --       ------"
	for _ in targetlist:
		print "  "+_+" "*(9-len(_))+targetlist[_]
	print

try:
	if desc == "get-id":
		print auto_help("BufferOverflow","Normal","Simple Remote BufferOverflow")
except:
	pass

def auto_info(name,module,plat,priv,lic,rank,release="N/A",by="N/A"):
	print "\nPublisher Information for %s" %name
	print
	print "       Name:",name
	print "     Module:",module
	print "   Platform:",plat
	print " Privileged:",priv
	print "    License:",lic
	print "       Rank:",rank
	print "  Disclosed:",release

def auto_opt(name,cset,req,description):
	stbl = "  " + name + " "*(9-len(name)) + cset + " "*(15-len(cset)+2) + req + " "*(8-len(req)+2) + description
	print stbl

try: BUF
except: BUF = 1024
try: RHOST
except: pass
try: RPORT
except: RPORT = 23
try: TIMEOUT
except: TIMEOUT = 5

def attack(RHOST,BUF=1025,RPORT=23,TIMEOUT=5):
	for _ in range(1):
		"Actions Here"
		pass

def show_opt():
	print "\nModule Options (Example)\n"
	print "  Name     Current Setting  Required  Description"
	print "  ----     ---------------  --------  -----------"
	try:
		auto_opt("BUF",str(BUF),"no","Buffer Size")
	except:
		auto_opt("BUF","  ","no","Total Buffer Size")
	try:
		auto_opt("RHOST",RHOST,"yes", "Target Host")
	except:
		auto_opt("RHOST","   ","yes", "Target Host")
	try:
		auto_opt("RPORT",str(RPORT),"yes", "Target Port")
	except:
		auto_opt("RPORT","   ","yes", "Target Port")
	try:
		auto_opt("TIMEOUT", str(TIMEOUT),"no", "Timeout Time")
	except:
		auto_opt("TIMEOUT","   ","no", "Timelout Time")
	print 

try:
	if desc == "get-opt":
		show_opt()
except:
	pass

try:
	if desc == "proc":
		try:
			if RHOST and RPORT and TIMEOUT and BUF:
				attack(RHOST,int(BUF),int(RPORT), int(TIMEOUT))
		except Exception as e:
			print e
			print "Options Still Unset"
			time.sleep(0.3)
			show_opt()
except:
	pass

try:
	if desc == "get-info":
		auto_info(name,"Example","Python 2.7","No","IDGAF License","Normal")
		show_opt()
		targets = {"1":"PacMan SSH","2":"Simple Socket Servers"}
		auto_targ(targets)
except:
	pass
