for x in [1,2,3]:
    for y in [1,2,3]:
        for z in [1,2,3]:
            if (x == 1 and y == 1) or z == 2:
                print "e,%s,%s,%s" % (x,y,z)
            else:
                print "p,%s,%s,%s" % (x,y,z)
