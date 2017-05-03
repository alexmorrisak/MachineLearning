# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys

#npoints = sys.argv[1]
nnets = 5


class net:
    def __init__(self, start, end, nnodes=2):
        self.intmdt = np.random.rand(nnodes-2, 2)
        self.nodes = np.vstack([start, self.intmdt, end])
        if end[0] < start[0]:
            self.nodes = self.nodes[::-1,:]
        self.start = self.nodes[0]
        self.end = self.nodes[-1]
        self.seg_route = np.ones(nnodes-1)
    def move_node(self, location, index=1):
        self.nodes[index,:] = location
    def insert_node(self, location, index=1):
        self.nodes = np.insert(self.nodes, index, location, axis=0)
        self.seg_route = np.append(self.seg_route,1)
    def get_node_angles(self):
        points = self.get_draw_points()
        node_angles = np.zeros(np.size(self.nodes,0)-2)
        for i, angle in enumerate(node_angles):
            x = points[2*i+2, 0]
            y = points[2*i+2, 1]
            dx0 = points[2*i+1,0] - x
            dy0 = points[2*i+1,1] - y
            dx1 = points[2*i+3,0] - x
            dy1 = points[2*i+3,1] - y
#            print dx0, dy0, dx1, dy1
            node_angles[i] = 180. / np.pi * np.arccos(
                (dx0 * dx1 + dy0 * dy1) /
                (np.sqrt(dx0**2 + dy0**2) * np.sqrt(dx1**2 + dy1**2)))
        return node_angles
    def straighten_route(self):
        nroutes = np.size(self.seg_route,0)
        route_options = np.zeros([2**nroutes, nroutes])
        for ir in range(0, 2**nroutes):
            for ic in range(0, nroutes):
                route_options[ir, ic] = ir % 2**(ic+1) / 2**ic
        angle_sums = np.zeros([2**nroutes])
        for ir in range(0, 2**nroutes):
            self.seg_route = route_options[ir, :]
            angle_sums[ir] = np.sum(self.get_node_angles())
#            print "route:", self.seg_route
#            print "cost: ", angle_sums[ir]
#            print "angles: ", self.get_node_angles()
#            print "draw points: ", self.get_draw_points()
#        print angle_sums
#        self.seg_route = [0, 0, 0]
#        print self.seg_route
#        print self.get_draw_points()
#        self.seg_route = [1, 1, 1]
#        print self.seg_route 
#        print self.get_draw_points()
#        print np.argmax(angle_sums)
#        print route_options[np.argmax(angle_sums)]
        self.seg_route = route_options[np.argmax(angle_sums)]
    def get_draw_points(self):
        draw_pts = np.zeros([(2*np.size(self.nodes,0) - 1), 2])
        draw_pts[0,:] = self.start
        draw_pts[-1,:] = self.end
        for iseg in range(0,len(self.seg_route)):
            s = [ self.nodes[iseg, 0], self.nodes[iseg, 1]]
            e = [ self.nodes[iseg+1, 0], self.nodes[iseg+1, 1]]
            if e[0] < s[0]:
                temp = s
                s = e
                e = temp
            delx = e[0] - s[0]
            dely = e[1] - s[1]
            if dely > 0:
                if dely > delx:
                    if self.seg_route[iseg] == 1:
                        intmdt = [ s[0], e[1]-delx ]
                    else:
                        intmdt = [ e[0], s[1]+delx ]
                else:
                    if self.seg_route[iseg] == 1:
                        intmdt = [ s[0]+dely, e[1] ]
                    else:
                        intmdt = [ e[0]-dely, s[1]]
            elif dely < 0:
                if np.abs(dely) > delx:
                    if self.seg_route[iseg] == 1:
                        intmdt = [ e[0], s[1]-delx ]
                    else:
                        intmdt = [ s[0], e[1]+delx ]
                else:
                    if self.seg_route[iseg] == 1:
                        intmdt = [ e[0]-np.abs(dely), s[1] ]
                    else:
                        intmdt = [ s[0]+np.abs(dely), e[1]]
            elif dely == 0:
                intmdt = [(e[0] + s[0]) / 2, e[1] ]

            draw_pts[2*iseg, :] = self.nodes[iseg,:]
            draw_pts[2*iseg+1,:] = intmdt
        return draw_pts
     
nets = [ net(np.random.rand(2), np.random.rand(2), 2) for i in range (0, 2)];
for net in nets:
    net.straighten_route()

#n = net([.1,.8], [.9,.90], 2)
#n.insert_node([.6,.1])
#n.insert_node([.4,.1])
#n.insert_node(np.random.rand(2))
#n.insert_node(np.random.rand(2))
#n.insert_node(np.random.rand(2))
#n.insert_node(np.random.rand(2))


#n.seg_route = [0, 0, 0]

#print n.nodes

#print n.intmdt
#print n.nodes
#a = n.get_draw_points()
#ang = n.get_node_angles()
#print "default route:", n.seg_route
#
#print "chosen route:", n.seg_route
##print ang
#print n.seg_route

#print np.size(a,0)
plt.figure()
for n in nets:
    plt.plot(n.start[0], n.start[1], 'x', ms=10)
    plt.plot(n.nodes[:,0], n.nodes[:,1], 'o')
    a = n.get_draw_points()

    plt.plot(a[:,0], a[:,1], linewidth=3, color='k')
    plt.grid()
    plt.xlim([0,1])
    plt.ylim([0,1])

sys.exit()    
#        self.points = np.sort(self.points, axis=0)

a = np.random.rand(nnets, 2)
#ay = np.random.rand(nnets)

b = np.random.rand(nnets, 2)
#by = np.random.rand(nnets)

plt.figure()


for ipt in range(0, nnets):
    s = [ a[ipt, 0], a[ipt, 1]]
    e = [ b[ipt, 0], b[ipt, 1] ]
    if b[ipt, 0] < s[0]:
        temp = s
        s = e
        e = temp
    delx = e[0] - s[0]
    dely = e[1] - s[1]
    if dely > 0:
        if dely > delx:
            intmdt = [ s[0], e[1]-delx]
        else:
            intmdt = [ e[0]-dely, s[1]]
    else:
        if np.abs(dely) > delx:
            intmdt = [ s[0], e[1]+delx]
        else:
            intmdt = [ e[0]+dely, s[1]]
#    net[ipt,:] = [s[0], intmdt[0], e[0]
    plt.plot(s[0], s[1], 'o')
    plt.plot(e[0], e[1], 'x')
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.grid()  
    plt.plot([s[0], intmdt[0], e[0]], [s[1], intmdt[1], e[1]])

#plt.plot()

