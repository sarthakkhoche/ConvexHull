import matplotlib.pyplot as plt
from random import randint
import numpy as np
import os, re, math, time, shutil
from PIL import Image, ImageDraw
from input import input

input = input()
arr = input.getCoordinates()
# input.quitInterface()

n1 = len(arr)
n2 = 20

CH = []
print("Point Set: " + str(arr))

directory = "jm/"
if not os.path.isdir(directory): 
    os.mkdir(directory)
else: 
    shutil.rmtree(directory) 
    os.mkdir(directory)

counter = 1

def plotPoints(P):
    plt.clf()
    plt.scatter(*zip(*arr))
    s = range(n2+1)

    plt.xticks(s)
    plt.yticks(s)

    plt.xlim([0, n2+1])
    plt.ylim([0, n2+1])
    plt.grid(True)

    # fname = str("points2.png")
    # plt.savefig(fname)
    
def findMin(P): #Inbuilt Function
    minX = P[0]
    for i in range(n1):
        if P[i][0] < minX[0]:
            minX = P[i]
    return minX        

def findMax(P):
    minX = P[0]
    for i in range(n1):
        if P[i][0] > minX[0]:
            minX = P[i]
    return minX     

globalMinCoord = findMin(arr)
globalMaxCoord = findMax(arr)    

def checking_pairs(minX, arr):
    global counter
    plt.scatter(*zip(*arr), color='blue')
    s = range(n2+1)

    plt.xticks(s)
    plt.yticks(s)

    plt.xlim([0, n2+1])
    plt.ylim([0, n2+1])
    plt.grid(True)
    
    for i in range(n1):
        small_arr = [minX, arr[i]]
        plt.plot(*zip(*small_arr), color='red')
        fname = str(directory + "im_" + str(counter) + "_" + str(minX[0]) + "_" + str(minX[1]) + "_" + str(i) + ".png")
        plt.savefig(fname)    
    counter += 1


def findAngleUH(a, b, p):
    global globalMinCoord
    if (p == globalMinCoord):
        vec = [b[0]-a[0], b[1]-a[1]]
        unit_vec1 = [0, 1]
        unit_vec2 = vec / np.linalg.norm(vec)
        dot_prod = np.dot(unit_vec1, unit_vec2)
        angle = np.arccos(dot_prod)
        angle = math.degrees(angle)
        return angle
    else:
        vec1 = [a[0]-p[0], a[1]-p[1]]
        vec2 = [b[0]-a[0], b[1]-a[1]]
        unit_vec1 = vec1 / np.linalg.norm(vec1)
        unit_vec2 = vec2 / np.linalg.norm(vec2)
        dot_prod = np.dot(unit_vec1, unit_vec2)
        angle = np.arccos(dot_prod)
        angle = math.degrees(angle)
        return angle


def findAngleLH(a, b, p):
    global globalMaxCoord
    if (p == globalMaxCoord):
        vec = [b[0]-a[0], b[1]-a[1]]
        unit_vec1 = [0, -1]
        unit_vec2 = vec / np.linalg.norm(vec)
        dot_prod = np.dot(unit_vec1, unit_vec2)
        angle = np.arccos(dot_prod)
        angle = math.degrees(angle)
        return angle
    else:    
        vec1 = [a[0]-p[0], a[1]-p[1]]
        vec2 = [b[0]-a[0], b[1]-a[1]]
        unit_vec1 = vec1 / np.linalg.norm(vec1)
        unit_vec2 = vec2 / np.linalg.norm(vec2)
        dot_prod = np.dot(unit_vec1, unit_vec2)
        angle = np.arccos(dot_prod)
        angle = math.degrees(angle)
        return angle

def findUpperClosestPoint(minX, arr, prevCoord):
    global counter

    for i in range(n1):
        if(minX != arr[i] and arr[i][0] >= minX[0]):
            minAngle = findAngleUH(minX, arr[i], prevCoord)
    
    index=0
    for i in range(n1):
        if(minX != arr[i] and arr[i][0] >= minX[0]):
            angle = findAngleUH(minX, arr[i], prevCoord)
            if(angle <= minAngle): 
                minAngle = angle
                index = i
    
    plt.scatter(*zip(*arr), color='blue')
    s = range(n2+1)

    plt.xticks(s)
    plt.yticks(s)

    plt.xlim([0, n2+1])
    plt.ylim([0, n2+1])
    plt.grid(True)
    
    plt.plot(*zip(*[minX, arr[index]]), color='green')
    fname = str(directory + "im_" + str(counter) + "_" + str(minX[0]) + "_" + str(minX[1]) + "_" + str(index) + ".png")
    plt.savefig(fname)
    counter += 1 
    return arr[index]    

def findLowerClosestPoint(maxX, arr, prevCoord):
    global counter
    
    for i in range(n1):
        if(maxX != arr[i] and maxX[0] >= arr[i][0]):
            minAngle = findAngleLH(maxX, arr[i], prevCoord)
    
    index=0
    for i in range(n1):
        if(maxX != arr[i] and maxX[0] >= arr[i][0]):
            angle = findAngleLH(maxX, arr[i], prevCoord)
            if(angle <= minAngle): 
                minAngle = angle
                index = i
    
    plt.scatter(*zip(*arr), color='blue')
    s = range(n2+1)

    plt.xticks(s)
    plt.yticks(s)

    plt.xlim([0, n2+1])
    plt.ylim([0, n2+1])
    plt.grid(True)
    
    plt.plot(*zip(*[maxX, arr[index]]), color='green')
    fname = str(directory + "im_" + str(counter) + "_" + str(maxX[0]) + "_" + str(maxX[1]) + "_" + str(index) + ".png")
    plt.savefig(fname)
    counter += 1 
    return arr[index]    

def findUCH(minX, arr, prevCoord):
    checking_pairs(minX, arr)
    updateX = findUpperClosestPoint(minX, arr, prevCoord)
    return updateX

def findLCH(maxX, arr, prevCoord):
    checking_pairs(maxX, arr)
    updateX = findLowerClosestPoint(maxX, arr, prevCoord)
    return updateX

# plotPoints(arr)    

start = time.time()

minCoord = findMin(arr)
CH.append(minCoord)
maxCoord = findMax(arr)

for i in range(n1):
    if(i==0): prevCoord = minCoord
    updateX = findUCH(minCoord, arr, prevCoord)
    CH.append(updateX)
    if(updateX == globalMaxCoord):
        break
    else:
        prevCoord = minCoord 
        minCoord = updateX

maxCoord = updateX
CH.append(maxCoord)

for i in range(n1):
    if(i==0): prevCoord = maxCoord
    updateX = findLCH(maxCoord, arr, prevCoord)
    CH.append(updateX)
    if(updateX == globalMinCoord):
        break
    else:
        prevCoord = maxCoord 
        maxCoord = updateX

CH = [list(t) for t in set(tuple(element) for element in CH)]
print("Convex Hull: " + str(CH))   

end = time.time()
print("Time taken: " + str(float("{0:.2f}".format(end-start))))

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

frames = []
for image in sorted_alphanumeric(os.listdir(directory)):
    frames.append(Image.open(directory + image))
frames[0].save(directory + 'output.gif', format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0)

# -------------------------------------------------------------------------

directory = "jm/output/"
os.mkdir(directory)

counter = 1
plotPoints(arr)

def findUCH(minX, arr, prevCoord):
    # checking_pairs(minX, arr)
    updateX = findUpperClosestPoint(minX, arr, prevCoord)
    return updateX

def findLCH(maxX, arr, prevCoord):
    # checking_pairs(maxX, arr)
    updateX = findLowerClosestPoint(maxX, arr, prevCoord)
    return updateX

minCoord = findMin(arr)
maxCoord = findMax(arr)

for i in range(n1):
    if(i==0): prevCoord = minCoord
    updateX = findUCH(minCoord, arr, prevCoord)
    if(updateX == globalMaxCoord):
        break
    else:
        prevCoord = minCoord 
        minCoord = updateX

maxCoord = updateX

for i in range(n1):
    if(i==0): prevCoord = maxCoord
    updateX = findLCH(maxCoord, arr, prevCoord)
    if(updateX == globalMinCoord):
        break
    else:
        prevCoord = maxCoord 
        maxCoord = updateX

frames = []
for image in sorted_alphanumeric(os.listdir(directory)):
    frames.append(Image.open(directory + image))
frames[0].save(directory + 'output.gif', format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0)

print("Done!")