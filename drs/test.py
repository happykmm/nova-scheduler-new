import commands

a,b = commands.getstatusoutput("echo '1 30 0' | ./drs03")
print a
print b

