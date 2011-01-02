#!/usr/bin/env python

def print_spiral(height,width):
    def getloop(x,y):
        if width-x < x:
            x=width-x+1
        if height-y < y:
            y=height-y+1
        if y < x:
            return y
        return x

    # Find max width of a number
    max=len(str(width*height))
    for y in range(height):
        for x in range(width):
            # current loop (get the current loop number)
            lo=getloop(x+1,y+1)
            # max-x
            mx=0
            # low-x
            lx=0
            # number
            nm=0

            # lpn = loop-number
            '''
            Find Lower and Max X
            '''
            for lpn in range(lo):
                lx=mx
                mx+=(width-(lpn*2))*2+(height-2-2*lpn)*2

            '''
            Determine the number for the given/current coordinate
            '''
            # Top
            if lo == y+1:
                nm = lx + 2 + x - lo
            # Left
            elif lo == x+1:
                nm = -y + lo + mx
            # Right
            elif lo == width - x:
                nm = lx + width - (lo*3) + y + 3
            # Bottom (horizontal)
            else:
                nm = lx + 2*width + height - lo*5 - x + 3
            print "%%%dd" % (max) % (nm),
        print ""
print print_spiral(5, 4)
