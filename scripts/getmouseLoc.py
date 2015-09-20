import commands
result =  commands.getstatusoutput('xdotool getmouselocation')

data = str(result).split(" ")
x = data[1].split(":")[1]
y = data[2].split(":")[1]
screen = data[3].split(":")[1]
window = data[4].split(":")[1]

print "x:" + x + " y:" + y
#print "y:" + y
#print "screen: " + screen
#print "window: " + window