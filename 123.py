ips = {}
modified=[]
fh = open("/root/Downloads/access.log", "r").readlines()
for line in fh:
    ip = line.split(" ")[0]
#    print len(ip)
    if 6 < len(ip) <=15:
        ips[ip] = ips.get(ip, 0) + 1

modified=sorted(ips.iteritems(), key = lambda x : x[1], reverse=True)

i=0
while(i<len(modified)):
    j=0
    print modified[i][j]+" : "+str(modified[i][j+1])
    i+=1


# print sorted(ips.itervalues(), reverse=True)
# print ips
# i=0
# for x in ips:
#    print x
#    print ips.get(x)
#    i+=1
