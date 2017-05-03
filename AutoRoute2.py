#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:03:11 2017

@author: alex
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import sys

RES = 1
XDIM = 100;
YDIM = XDIM;
NNETS =2
startx, starty = np.random.randint(0, XDIM, 2)
startx, starty = [10,8]
endx, endy = np.random.randint(0, XDIM,2)
#endx, endy = [10,15]

class linkedItem:
    def __init__(self, point):
        self.value = point
        self.next = None
        self.previous = None



graph = np.zeros([XDIM / RES, YDIM / RES])
nodes = range(0, XDIM*YDIM)
badnodes = []
#badnodes = range(105,115) + range(205,215)

def gridToSerial(gridx, gridy, xdim, ydim):
    return gridx + gridy*xdim

def serialToGrid(serial, xdim, ydim):
    gridx = serial % xdim
    gridy = serial / xdim
    return gridx, gridy
    
def findAdjacentNodes(node, nodes, xdim, ydim):
    gridx, gridy = serialToGrid(node, xdim, ydim)
    conn = []
    if gridx == 0:
        gridleft = 0
    else:
        gridleft = gridx - 1
    if gridx == xdim-1:
        gridright = xdim - 1
    else:
        gridright = gridx + 1
    if gridy == 0:
        gridlower = 0
    else:
        gridlower = gridy - 1
    if gridy == ydim-1:
        gridupper = ydim - 1
    else:
        gridupper = gridy + 1
        
    connNodes = []
    for x in range(gridleft, gridright+1):
        for y in range(gridlower, gridupper+1):
            newNeighbor = gridToSerial(x,y,xdim,ydim)
            if node in badnodes or newNeighbor in badnodes:
                cost = 100
            else:
                cost = 1
            if x != gridx and y != gridy:
                connNodes.append([newNeighbor, cost*2**.5])
#                    connNodes.append([newNode, 100])
            else:
                connNodes.append([newNeighbor, cost*1])
    return connNodes
    
def changeCost(node, conn):
    tic = time.time()
    newConn = conn
    for neighbor in newConn[node]:
        neighbor[1] = float('inf')
        nneighbors = [ val[0] for val in conn[int(neighbor[0])] ]
        nninx = nneighbors.index(neighbor[0])
        newConn[neighbor[0]][nninx][1] = float('inf')
    return newConn
        

# Build connection dictionary for each node
tic = time.time()
conn = dict()
for node in nodes:
    conn[node] = findAdjacentNodes(node, nodes, XDIM, YDIM)
print time.time() - tic, " sec elapsed"

def argmin(iterable):
    return min(enumerate(iterable), key=lambda x: x[1])[0]
    
def dijkstra(nodes, edges, start, end):
    unvisited = nodes[:]
    dist = [float('inf')] * len(nodes)
    prev = [None] * len(nodes)
    
    dist[start] = 0
    while unvisited:
        node = unvisited[argmin(dist[int(i)] for i in unvisited)]
        del unvisited[unvisited.index(node)]
        if node == end: 
            break
        for neighbor in edges[node]:
            alt = dist[node] + neighbor[1]
            if alt < dist[neighbor[0]]:
                dist[neighbor[0]] = alt
                prev[neighbor[0]] = node
                
    return dist, prev

def h(current, target, xdim, ydim):
    x, y = serialToGrid(current, xdim, ydim)
    xx, yy = serialToGrid(target, xdim, ydim)
    return ((xx-x)**2 + (yy-y)**2)**0.5
# Nodes evaluated using cost function f(x) = g(x) + h(x)
# where g is the actual weighted-distance cost to the current
# node and h is the heuristic estimate of current node to
# finish (straight-line euclicdean distance)
def astar(nodes, edges, start, end, xdim, ydim):
    unvisited = nodes[:]
    openSet = [start]
    closedSet = []
    g = [float('inf')] * len(nodes)
    f = [float('inf')] * len(nodes)

    prev = [None] * len(nodes)
    
    g[start] = 0
#    f[start] = h(start, end, xdim, ydim)
    head = linkedItem([start, h(start, end, xdim, ydim)])
    node = start
    icalcs = 0
    item = head
    while item:
        # sort the open set or something instead of re-calculating
        # the f() value EVERY FUCKING TIME!!!
        #node = openSet[argmin(f[int(i)] for i in openSet)]
        node = item.value[0]
        print 'node:',  node
        #print '\n', "func inx", func[0]
        #del openSet[openSet.index(node)]
        #x = [x for x in func if node in x][0]
        #print "x:", x.index(node)
        #xinx = x.index(node)
        head.previous = None
        closedSet.append(node)
        if node == end: 
            break
        for neighbor in edges[node]:
            icalcs = icalcs+1

            print '\r', icalcs, h(node, end, xdim, ydim),
            #print serialToGrid(neighbor[0], XDIM, YDIM)
            if neighbor[0] in closedSet:
                continue
            alt = g[node] + neighbor[1]
            #if neighbor[0] not in openSet:
            #    openSet.append(neighbor[0])
            if alt < g[neighbor[0]]:
                g[neighbor[0]] = alt
                f[neighbor[0]] = alt + h(node, end, xdim, ydim)
                newh = alt + h(node,end,xdim,ydim)
#                item = head
                while item:
                    print 'yes', item
                    if newh < item.value[1]:
                        print '\nfound!:',
                        newitem = linkedItem([neighbor[0], newh])
                        newitem.previous = item.previous
                        newitem.next = item
                        (item.previous).next = newitem
                        item.previous = newitem
                        break
                    item = item.next
                if item.next == None:
                    newitem = linkedItem([neighbor[0], newh])
                    item.next = newitem
                    newitem.previous = item
               #print func
                prev[neighbor[0]] = node
                
    #print serialToGrid(node, XDIM, YDIM), serialToGrid(end, XDIM, YDIM)
    if node != end:
        print "error, did not find path to end"

    return g, prev

def backtrack(prev, source, target):
    path = [target]
    u = target
    while prev[u]:
        path = [prev[u]] + path
        u = prev[u]
    path = [source] + path
    return path

def fillwidth(path, width, xdim, ydim):
    fill = path[:]
    for pt in path:
        gridx,gridy = serialToGrid(pt, xdim, ydim)
        if (gridx - width) < 0:
            gridleft = 0
        else:
            gridleft = gridx - width
        if (gridx + width) > (xdim - 1):
            gridright = xdim - 1
        else:
            gridright = gridx + width
        if (gridy - width) < 0:
            gridlower = 0
        else:
            gridlower = gridy - width
        if (gridy + width) > (ydim-1):
            gridupper = ydim - 1
        else:
            gridupper = gridy + width
        for x in range(gridleft, gridright+1):
            for y in range(gridlower, gridupper+1):
                fill.append(gridToSerial(x,y,xdim,ydim))
    return set(fill)

#for pt in fill:
#    conn = changeCost(pt, conn)

starts = []
ends = []

paths = [];
keepouts = set()
traces = set()
for inet in range(0,NNETS):
    x,y = np.random.randint(10, XDIM-10,2)
    xx,yy = np.random.randint(10, XDIM-10,2)
    start = gridToSerial(x,y, XDIM, YDIM)
    end = gridToSerial(xx,yy, XDIM, YDIM)
    if start in keepouts or end in keepouts:
        continue
    dist, prev = astar(nodes, conn, start, end, XDIM, YDIM)
    path = backtrack(prev, start, end)
    print "path len:", len(path)
    if len(path) == 2:
        print path
    paths.append(path)
    keepout = fillwidth(path, 5, XDIM, YDIM)
    trace = fillwidth(path, 1, XDIM, YDIM)
    for pt in keepout:
        conn = changeCost(pt, conn)
    keepouts = keepouts | keepout
    traces = traces | trace


    
image = np.zeros([XDIM, YDIM])
for path in paths:
    for point in traces:
        x,y = serialToGrid(point, XDIM, YDIM)
        image[x,y] = 1

    
plt.imshow(image.T, interpolation='none')
plt.show()

distGrid = np.array(dist)
distGrid = np.reshape(dist, [XDIM, YDIM])
#plt.imshow(distGrid.T, interpolation='none')



#print conn.keys()[conn.values().index(0)] # Prints george
#
#
#class net:
#    def __init__(self, _start, _end):
#        self.nodes = np.vstack([_start, _end])
#    def add_node(self, _node):
#        self.nodes = np.vstack([self.nodes, _node])
#
#n = net([1,1], [2,2])
#
#print n.nodes
#
#class Graph:
#    __init__(self, xdim, ydim):
#        self.nodes = np.zeros([xdim, ydim])
#        self.edges = np.zeros([xdim, ydim, 8])
#        self.
#    
#graph[100,:] = 1
#
#plt.figure()
#plt.imshow(graph)
