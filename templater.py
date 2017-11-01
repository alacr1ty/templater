#!/usr/bin/python
import time,sys,os,csv,re,shutil

def template (content):
	tmp = "./template.fdr"
	if "default" in content:
		out = "./output.html"
		shutil.copyfile(tmp,out)
	else:
		out = "./output/"+content.split("/")[-1].split(".")[0]+".html"
		with open(content) as f:
			readf = f.readlines()
		with open(tmp) as t:
			readt = t.readlines()
		with open(out,'w') as o:
			for linet in readt:
				if "<!-- TEMPLATE PAUSES HERE -->" in linet:
					# switch to content fodder file
					o.write(linet)
					for linef in readf:
						o.write(linef)
				else:
					o.write(linet)
	return

def uerror (err_n):
	if err_n is 1:
		print "Usage: ./templater.py {fodder.fdr | default}"
	elif err_n is 2:
		print "Error: Missing .fdr file!"
	exit(1)

if __name__ == '__main__':
	# if there is already an output file, log it away
	if os.path.isfile("./output.html"):
		shutil.move("./output.html","./logs/output"+str(time.time())+".html")
		# we could have output files match input prefixes
	if os.path.isdir("./output/"):
		shutil.move("./output/","./logs/output"+str(time.time())+"/")
	os.mkdir("./output/")

	if len(sys.argv) is 2:
		if "." in sys.argv[1]:
			if sys.argv[1].split(".")[-1] in "fdr":
				if os.path.isfile(sys.argv[1]):
					template(sys.argv[1])
				else:
					uerror(2)
			else:
				uerror(2)
		elif sys.argv[1] in "default":
			template(sys.argv[1])
		else:
			uerror(1)
	elif len(sys.argv) is 1:
		for (dirpath,dirnames,filenames) in os.walk("./fodder/"):
			for file in filenames:
				if file:
					template("./fodder/"+file)
	else:
		uerror(1)

	exit(0)
