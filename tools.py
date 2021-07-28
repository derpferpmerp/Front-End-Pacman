import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from numpy.random import randint as rnd
import math

def maze(width=81, height=51, complexity=.75, density =.75, b=True, bl=False):
	if b:
		shape = ((height//2)*2 + 1, (width//2)*2 + 1)
	else:
		shape = ((height//2)*2, (width//2)*2)
	complexity = int(complexity*(5*(shape[0]+shape[1])))
	density    = int(density*(shape[0]//2*shape[1]//2))
	Z = np.zeros(shape, dtype=bool)
	if b:
		Z[0,:] = Z[-1,:] = 1
		Z[:,0] = Z[:,-1] = 1
	for i in range(density):
		x, y = rnd(0,shape[1]//2)*2, rnd(0,shape[0]//2)*2
		Z[y,x] = 1
		for j in range(complexity):
			neighbours = []
			if x > 1:           neighbours.append( (y,x-2))
			if x < shape[1]-2:  neighbours.append( (y,x+2))
			if y > 1:           neighbours.append( (y-2,x))
			if y < shape[0]-2:  neighbours.append( (y+2,x))
			if len(neighbours):
				y_,x_ = neighbours[rnd(0,len(neighbours)-1)]
				if Z[y_,x_] == 0:
					Z[y_,x_] = 1
					Z[y_+(y-y_)//2, x_+(x-x_)//2] = 1
					x, y = x_, y_
	return [1 * Z if not bl else Z][0]

def gen_maze_img(w=10,h=10,c=0.75,d=0.75,brdr=True,m=0.5,bl2=False,grid=False):
	plt.figure(figsize=(10,10),dpi=100)
	cmap = colors.ListedColormap(["black", "white","#39ff14","red"])
	bounds=[0,0.9,1.9,2.9,3.9]
	norm = colors.BoundaryNorm(bounds, cmap.N)
	if type(grid) == type(True):
		mzgenned = maze(width=w,height=h,complexity=c,density=d,b=brdr,bl=bl2)
	else:
		mzgenned = grid
	plt.imshow(mzgenned,cmap=cmap,norm=norm,interpolation="nearest")
	plt.xticks([]),plt.yticks([])
	plt.savefig("lvl.png")
	return mzgenned * 1

def get_endless_difficulty(currentlevel,mx=1,modif=1,dplaces=2,method="SIGMOID"):
	if mx != 1 and mx < 1 and mx > 0:
		mx = 1 / mx
	if method == "SIGMOID":
		return round((1)/(mx + math.exp(-1 * (1/modif) * (currentlevel))),dplaces)

"""
def rateofchange(lst):
	lstvals = []
	for x in range(len(lst)-1):
		if x == 0: continue
		try:
			lstvals.append(lst[x+1]/lst[x])
		except IndexError:
			continue
	return f"{round(100 * (sum(lstvals) / len(lstvals)))/100}x"

def delta(lst):
	lstvals = []
	for x in range(len(lst)-1):
		try:
			lstvals.append(lst[x+1] - lst[x])
		except IndexError:
			continue
	return round(sum(lstvals) / len(lstvals), 2)

cllist = [0]
cl = 0
maxval = 0.5
modifier = 1
untilpercent = 98

while cllist[-1] < (untilpercent*maxval)/100:
	cllist.append(get_endless_difficulty(cl,mx=maxval,modif=modifier))
	cl += 1

print(f"Amount of Iterations: {len(cllist)}\nAverage Rate of Change: {rateofchange(cllist)}\nAverage Difference: {delta(cllist)}\nList: {cllist}")"""