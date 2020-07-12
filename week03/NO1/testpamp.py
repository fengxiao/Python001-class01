import os
commamd = "pmap.py -n 4 -f ping -ip 192.168.10.1-192.168.10.20"
print(commamd)
mreturn = os.system(commamd)

# commamd = "pmap.py -n 4 -f tcp -ip 192.168.30.16"
# print(commamd)
# mreturn = os.system(commamd)

