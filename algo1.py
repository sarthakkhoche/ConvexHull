import matplotlib.pyplot as plt
from random import randint
import numpy as np
import os, re, time, math, shutil
from PIL import Image, ImageDraw
from input import input

input = input()
arr = input.getCoordinates()
# input.quitInterface()

n1 = len(arr)
n2 = 20

CH = []
print("Point Set: " + str(arr))

directory = "slowalgo/"
if not os.path.isdir(directory): 
    os.mkdir(directory)
else: 
    shutil.rmtree(directory) 
    os.mkdir(directory)

def plotPoints(P):
    plt.clf()
    plt.scatter(*zip(*P))
    s = range(n2+1)

    plt.xticks(s)
    plt.yticks(s)

    plt.xlim([0, n2+1])
    plt.ylim([0, n2+1])
    plt.grid(True)
    
    # fname = str("points1.png")
    # plt.savefig(fname)

def checking_pairs(arr, small_arr, i, j):
    plt.scatter(*zip(*arr), color='blue')
    s = range(n2+1)

    plt.xticks(s)
    plt.yticks(s)

    plt.xlim([0, n2+1])
    plt.ylim([0, n2+1])
    plt.grid(True)

    plt.plot(*zip(*small_arr), color='red')
    fname = str(directory + "im_" + str(i) + "_" + str(j) + "_1.png")
    plt.savefig(fname)

def check_right(arr, i, j):
    if(((arr[i][0]-arr[j][0])) != 0): slope = (arr[i][1]-arr[j][1])/float((arr[i][0]-arr[j][0]))
    else: slope = math.inf

    for v in range(n1):
        if(v!=i and v!=j):
            value = arr[v][1] - arr[i][1] - slope*(arr[v][0] - arr[i][0])
            check = np.sign(value)
            break
    
    for v in range(n1):
        if(v!=i and v!=j):
            value = arr[v][1] - arr[i][1] - slope*(arr[v][0] - arr[i][0])
            check_v = np.sign(value)
            if(check_v!=check): 
                return 0
    return 1

def add_pairs(arr, i, j):
    plt.scatter(*zip(*arr), color='blue')
    s = range(n2+1)

    plt.xticks(s)
    plt.yticks(s)

    plt.xlim([0, n2+1])
    plt.ylim([0, n2+1])
    plt.grid(True)
    
    if(check_right(arr, i, j)):
        plt.plot(*zip(*[arr[i], arr[j]]), color='green')
        fname = str(directory + "im_" + str(i) + "_" + str(j) + "_2.png")
        plt.savefig(fname)
        return arr[i], arr[j], 1
    else:
        return arr[i], arr[j], 0   

# plotPoints(arr) 

start = time.time()

for i in range(n1):
    for j in range(i+1, n1):
        if(i!=j):
            checking_pairs(arr, [arr[i], arr[j]], i, j)
            a, b, v = add_pairs(arr, i, j)
            if(v==1): 
                CH.append(a)
                CH.append(b)

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

directory = "slowalgo/output/"
os.mkdir(directory)

plotPoints(arr) 

for i in range(n1):
    for j in range(i+1, n1):
        if(i!=j):
            a, b, v = add_pairs(arr, i, j)
            if(v==1): 
                CH.append(a)
                CH.append(b)

frames = []
for image in sorted_alphanumeric(os.listdir(directory)):
    frames.append(Image.open(directory + image))
frames[0].save(directory + 'output.gif', format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0)

print("Done!")