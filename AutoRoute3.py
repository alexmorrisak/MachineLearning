#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:08:19 2017

@author: alex
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import itertools
import sys
import copy

LW = 3
#nnets = 10
#nnodes = 10

class net:
    def __init__(self, start, end):
        self.nodes = np.empty((3,2))
        self.nodes[0,:] = start
        self.nodes[1,0] = start[0]
        self.nodes[1,1] = end[1]
        self.nodes[2,:] = end
    def get_segments(self):
        segments = np.empty((np.size(self.nodes,0)-1,2,2))
        #print 'seg size:', np.shape(segments)
        #print 'nodes size:', np.shape(self.nodes)
        for inode in range(0,np.size(self.nodes,0)-1):
            segments[inode, :, 0] = \
                [self.nodes[inode,0], self.nodes[inode+1,0]]
            segments[inode, :, 1] = \
                [self.nodes[inode,1], self.nodes[inode+1,1]]
        return segments
    def get_distance_to_edge(self, x, y):
        dEnd = np.sqrt((y-self.nodes[-1,1])**2 + (x-self.nodes[-1,0])**2)
        dStart = np.sqrt((y-self.nodes[0,1])**2 + (x-self.nodes[0,0])**2)
        if dStart < dEnd:
            return dStart
        else:
            return dEnd
    def get_nodes(self):
        return self.nodes
    def get_length(self):
        l = 0
        segs = self.get_segments()
        for seg in segs:
            l = l + np.sqrt((seg[0,0] - seg[1,0])**2 + (seg[0,1]-seg[1,1])**2)
        return l
    def flip_corner(self):
        if len(self.get_segments()) == 2:
            if self.nodes[1,0] == self.nodes[0,0]:
                self.nodes[1,1] = self.nodes[0,1]
                self.nodes[1,0] = self.nodes[2,0]
            else:
                self.nodes[1,1] = self.nodes[2,1]
                self.nodes[1,0] = self.nodes[0,0]
    def add_segment(self):
        nsegs = len(self.get_segments())
        iseg = np.random.randint(0,nsegs)
        if self.nodes[iseg,1] == self.nodes[iseg+1,1]:
            h = True
            fix = self.nodes[iseg, 1]
        else:
            h = False
            fix = self.nodes[iseg, 0]
        if h:
            minSpan = np.min([self.nodes[iseg,0], self.nodes[iseg+1,0]])
            maxSpan = np.max([self.nodes[iseg,0], self.nodes[iseg+1,0]])
            newNode = [np.random.uniform(minSpan, maxSpan), fix]
        else:
            minSpan = np.min([self.nodes[iseg,1], self.nodes[iseg+1,1]])
            maxSpan = np.max([self.nodes[iseg,1], self.nodes[iseg+1,1]])
            newNode = [fix, np.random.uniform(minSpan, maxSpan)]
        self.nodes = np.insert(self.nodes, iseg+1, newNode, axis=0)
    def insert_segpair(self):
        nsegs = len(self.get_segments())
        iseg = np.random.randint(0,nsegs)
        if self.nodes[iseg,1] == self.nodes[iseg+1,1]:
            h = True
            fix = self.nodes[iseg, 1]
        else:
            h = False
            fix = self.nodes[iseg, 0]
        if h:
            minSpan = np.min([self.nodes[iseg,0], self.nodes[iseg+1,0]])
            maxSpan = np.max([self.nodes[iseg,0], self.nodes[iseg+1,0]])
            newNode = [np.random.uniform(minSpan, maxSpan), fix]
        else:
            minSpan = np.min([self.nodes[iseg,1], self.nodes[iseg+1,1]])
            maxSpan = np.max([self.nodes[iseg,1], self.nodes[iseg+1,1]])
            newNode = [fix, np.random.uniform(minSpan, maxSpan)]
        self.nodes = np.insert(self.nodes, iseg+1, newNode, axis=0)
        self.nodes = np.insert(self.nodes, iseg+1, newNode, axis=0)
    def rotate_endpoint(self):
        nsegs = len(self.get_segments())
        iseg = 0
        testroll = np.random.randint(0,2)
        # Rotate the starting node point
        if testroll == 1:
            if self.nodes[iseg,1] == self.nodes[iseg+1,1]: # segment is horizontal
                newNode = copy.deepcopy(self.nodes[iseg,:])
                newNode[1] = newNode[1] + 1e-6
                self.nodes[iseg+1,1] = self.nodes[iseg+1,1] + 1e-6
                self.nodes = np.insert(self.nodes, iseg+1, newNode, axis=0)
            else:
                newNode = self.nodes[iseg,:]
                newNode[0] = newNode[0] + 1e-6
                self.nodes[iseg+1,0] = self.nodes[iseg+1,0] + 1e-6
                self.nodes = np.insert(self.nodes, iseg+1, newNode, axis=0)
        else:
            if self.nodes[-1,1] == self.nodes[-2,1]: # segment is horizontal
                newNode = copy.deepcopy(self.nodes[-1,:])
                newNode[1] = newNode[1] + 1e-6
                self.nodes[-2,1] = self.nodes[-2,1] + 1e-6
                self.nodes = np.insert(self.nodes, -1, newNode, axis=0)
            else:
                newNode = self.nodes[-1,:]
                newNode[0] = newNode[0] + 1e-6
                self.nodes[-2,0] = self.nodes[-2,0] + 1e-6
                self.nodes = np.insert(self.nodes, -1, newNode, axis=0)
    # Combine two nodes, effectively reducing the number of segments and complexity of the board
    def fuse_nodes(self):
        if self.nodes[0,1] == self.nodes[1,1]:
            h = True
        else:
            h = False
        nsegs = len(self.get_segments())
        if nsegs > 3:
            iseg = np.random.randint(1,nsegs-2)
            if (iseg % 2 == 0 and h) or (iseg % 2 == 1 and not h): # this particular seg is horizontal
                self.nodes[iseg,1] = self.nodes[iseg+3,1]
            else: # this particular seg is vertical
                self.nodes[iseg,0] = self.nodes[iseg+3,0]
            self.nodes = np.delete(self.nodes, iseg+1, axis=0) 
            self.nodes = np.delete(self.nodes, iseg+1, axis=0) 

    # Pick a particular segment at random and move it to the left/right or up/down a random amount 
    def mutate_segment(self, p_move=.1, magnitude=.2):
        diceroll = np.random.rand()
        if diceroll < p_move:
            nsegs = len(self.get_segments())
            if self.nodes[0,1] == self.nodes[1,1]:
                h = True
            else:
                h = False
            if nsegs > 3:
                iseg = np.random.randint(1,nsegs-1)
                if (iseg % 2 == 0 and h) or (iseg % 2 == 1 and not h): # this particular seg is horizontal
                    y = self.nodes[iseg,1]
                    y = y + magnitude*np.random.randn()
                    self.nodes[iseg,1] = y
                    self.nodes[iseg+1,1] = y
                else: # this particular seg is vertical
                    h = False
                    x = self.nodes[iseg,0]
                    x = x + magnitude*np.random.randn()
                    self.nodes[iseg,0] = x
                    self.nodes[iseg+1,0] = x


def get_all_segments(nets):
    segToNet = dict()
    allsegs = np.empty([0,2,2])
    for inet, n in enumerate(nets):
        segs = n.get_segments()
        for iseg in range(0,np.size(segs,0)):
            segToNet[np.size(allsegs,0) + iseg] = inet
        allsegs = np.vstack([allsegs, segs])
    return segToNet, allsegs
    

        
def find_intersections(segs):
    nsegs = np.size(segs,0)
    inters = list()
    for iseg in range(0,nsegs-1):
    #    print allsegs[iseg]
    ##    print allsegs[j]
        if segs[iseg,0,1] == segs[iseg,1,1]: # primary seg is horizontal
            h = True
        else:
            h = False
        for j in range(iseg+1, nsegs):
            if segs[j,0,1] == segs[j,1,1]: # secondary seg is vertical
                if h:
                    continue
                else:
                    intersect = True
            else:
                if h:
                    intersect = True
                else:
                    continue
            if intersect:
                if np.equal(segs[iseg,0], segs[j,0]).all() or \
                    np.equal(segs[iseg,0], segs[j,1]).all() or \
                    np.equal(segs[iseg,1], segs[j,0]).all() or \
                    np.equal(segs[iseg,1], segs[j,1]).all():
                    continue
                else:
                    if h:
                        minx = np.min(segs[iseg,:,0])
                        maxx = np.max(segs[iseg,:,0])
                        miny = np.min(segs[j,:,1])
                        maxy = np.max(segs[j,:,1])
                    else:
                        miny = np.min(segs[iseg,:,1])
                        maxy = np.max(segs[iseg,:,1])
                        minx = np.min(segs[j,:,0])
                        maxx = np.max(segs[j,:,0])
                                        
                    if h:
                        x = segs[j,0,0]
                        y = segs[iseg,0,1]
                        if (y > miny and y < maxy) and \
                            (x > minx and x < maxx):
                                inter = (iseg, j, x, y, )
                                inters.append(inter)

                    else:
                        x = segs[iseg,0,0]
                        y = segs[j,0,1]
                        if (y > miny and y < maxy) and \
                            (x > minx and x < maxx):
                                inter = (iseg, j, x, y, )
                                inters.append(inter)
    return inters

# Calculate the cost of the board using all nets as input
def find_cost(nets):
    t0 = time.time()
    segToNet, segs = get_all_segments(nets)
    inters = find_intersections(segs)
    t1 = time.time()

    # Calculate total trace length
    totalLen = 0
    t0 = time.time()
    for net in nets:
        totalLen = totalLen + net.get_length()
    t1 = time.time()
    
    t0 = time.time()
    # Calculate intersection point to edge of segment
    totalD2E = 0
    for inter in inters:
        net = segToNet[inter[0]]
        dToE = nets[segToNet[inter[0]]].get_distance_to_edge(inter[2],inter[3])
        altDToE = nets[segToNet[inter[1]]].get_distance_to_edge(inter[2],inter[3])
        if altDToE < dToE:
            dToE = altDToE
        totalD2E = totalD2E + dToE
      
    t1 = time.time()
    return 100*np.sqrt(totalD2E) + totalLen

# Mutate the entire system using parameterized probability of mutation for each type of mutation
def mutate_system(system, p_flip = 0.05, p_insertseg = 0.05, p_fuseseg = 0.06, p_rotateend = .05, p_move=0.5):
    for net in system:
        diceroll = np.random.uniform(0,1,[4])
        if diceroll[0] < p_flip:
            net.flip_corner()
        if diceroll[1] < p_insertseg:
            net.insert_segpair()
        if diceroll[2] < p_fuseseg:
            net.fuse_nodes()
        if diceroll[3] < p_rotateend:
            net.rotate_endpoint()
        net.mutate_segment(p_move = p_move)
    return system

def crossover(a, b):
    a = copy.deepcopy(b)
    nnets = len(a)
    diceroll = np.random.randint(0,2,[nnets])
    inx = np.where(diceroll == 1)
    a[inx] = copy.deepcopy(b[inx])
    return a
    
    
NNETS=10
POP=80
points_sx = np.random.uniform(5,25,[NNETS, 1,1]) / 50
points_sy = np.random.uniform(5,45,[NNETS, 1,1]) / 50
points_s = np.concatenate([points_sx, points_sy], axis=2)
points_ex = np.random.uniform(25,45,[NNETS, 1,1]) / 50
points_ey = np.random.uniform(5,45,[NNETS, 1,1]) / 50
points_e = np.concatenate([points_ex, points_ey], axis=2)
points = np.concatenate([points_s, points_e], axis = 1)
points = np.random.uniform(5,45,[NNETS, 2, 2]) / 50
systems = [ [net(points[i, 0,:], points[i, 1,:]) for i in range(NNETS) ] for _ in range(POP) ]
systems = np.array(systems)

plt.ion()
plt.figure()

for system in systems:
    system = mutate_system(system, p_flip = 0.1, p_insertseg = 0.1)

nets = copy.deepcopy(systems[0])
segToNet, segs = get_all_segments(nets)
inters = find_intersections(segs)

cost = find_cost(nets)
print 'Total cost:', cost
#t1 = time.time()
#print 'Elapsed time for full function: ', t1-t0

for iseg in range(0,np.size(segs,0)):
    plt.plot(segs[iseg,:,0], segs[iseg,:,1],\
             color = 'k',\
             linewidth =LW)
for inter in inters:
    plt.plot(segs[inter[0], :, 0], segs[inter[0], :, 1], \
        color = 'r',\
        linewidth = LW)
    plt.plot(segs[inter[1], :, 0], segs[inter[1], :, 1], \
        color = 'r',\
        linewidth = LW)
plt.xlim([0,1])
plt.ylim([0,1])
plt.grid()
plt.title(['Total Cost:', cost])
print 'Pausing for 10 seconds before starting...'
plt.pause(10)
# Main event loop where we search for a good solution to the routing problem
generation = 0
while True:
    generation = generation + 1
    print 'generation:', generation
    plt.clf()
    costs = np.empty([len(systems)], dtype='float')

    # Find cost of each member of the population and sort by cost (lowest-to-highest)
    t0 = time.time()
    for isys in range(0,POP):
        system = systems[isys]
        costs[isys] = find_cost(system)
    costRank = np.argsort(costs)
    systems = copy.deepcopy(systems[costRank])
    costs = copy.deepcopy(costs[costRank])
    print costs
    nets = copy.deepcopy(systems[0])
    t1 = time.time()
    print 'Elapsed time: ', t1-t0


    # Perform genetic algorithm.  Crossover, mutation, and culling
    #for isys in range(0,POP/4):
    #    child = crossover(systems[isys], systems[POP/4+isys])
    #    systems[2*POP/4+isys] = copy.deepcopy(child)
    #for isys in range(0,POP/4): # small mutations to already good population
    #    child = crossover(systems[isys], systems[POP/4+isys])
    #    systems[3*POP/4+isys] = copy.deepcopy(child)
    #    systems[3*POP/4+isys] = mutate_system(systems[3*POP/4+isys])
    #    #systems[ = mutate_system(system)
    for isys in range(0,POP/2):
        #systems[1*POP/2+isys] = copy.deepcopy(systems[isys])
        systems[1*POP/2+isys] = crossover(systems[2*isys], systems[2*isys+1])
    for isys in range(POP/4,POP):
        systems[isys] = mutate_system(systems[isys],.1,.05,.1)
    temp = crossover(systems[0], systems[1])
    systems[1*POP/4] = copy.deepcopy(temp)
    #systems[isys] = mutate_system(systems[isys],.1,.05,.1)

    #for isys in range(0,POP):
    #    system = systems[isys]
    #    costs[isys] = find_cost(system)
    #costRank = np.argsort(costs)
    #systems = copy.deepcopy(systems[costRank])

    #for isys in range(0,POP):
    #    system = systems[isys]
    #    costs[isys] = find_cost(system)
    #print 'costs, after mutation:', costs

    #print 'cost rank:', costRank
    #systems[costRank[POP/2-1:-1]] = copy.deepcopy(systems[costRank[0:POP/2]])
    #print systems
    #for isys in range(0,POP):
    #    system = systems[isys]
    #    costs[isys] = find_cost(system)
    #print 'costs, after culling:', costs

    segToNet, segs = get_all_segments(nets)
    inters = find_intersections(segs)

    cost = find_cost(nets)
    print 'Total cost:', cost
    t1 = time.time()
    print 'Elapsed time for full function: ', t1-t0

    for iseg in range(0,np.size(segs,0)):
        plt.plot(segs[iseg,:,0], segs[iseg,:,1],\
                 color = 'k',\
                 linewidth =LW)
    for inter in inters:
        plt.plot(segs[inter[0], :, 0], segs[inter[0], :, 1], \
            color = 'r',\
            linewidth = LW)
        plt.plot(segs[inter[1], :, 0], segs[inter[1], :, 1], \
            color = 'r',\
            linewidth = LW)
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.grid()
    plt.title(['Total Cost:', cost])
    plt.pause(.1)
    t1 = time.time()
    print 'Elapsed time: ', t1-t0
