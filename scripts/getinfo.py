import platform
#print platform(aliased=0, terse=0)
#print machine()
print 'uname:', platform.uname()

print
print 'system   :', platform.system()
print 'node     :', platform.node()
print 'release  :', platform.release()
print 'version  :', platform.version()
print 'machine  :', platform.machine()
print 'processor:', platform.processor()
print 'interpreter:', platform.architecture()
print '/bin/ls    :', platform.architecture('/bin/ls')