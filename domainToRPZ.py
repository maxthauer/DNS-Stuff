#!/usr/local/bin/python3

'''
Take a list of domains and convert it to a list of BIND zones so
apply DNS-RPZ to domains in the list.

By Max Thauer
_
Example list:

domain.tld
www.domain.tld
...
...
mydomain.tld
_
Example output:

zone "domain.tld"  {type master; file "/etc/bind/rpz/blocked.zone";}; 
_
'''
import os, time

startTime = time.time()

f = open('list.txt')
o = open('out.txt', 'w')
i = 0

for line in f:
	rpzA = "zone \""
	rpzB = "\"  {type master; file \"/etc/bind/rpz/blocked.zone\";};"
	line = line.replace('\n','')
	o.write (rpzA+line+rpzB+"\n")
	i = i + 1

f.close
o.close

endTime = time.time()
timeDiff = endTime-startTime
print ("Processed {} lines in {} seconds.".format(i,timeDiff))