import time 
from math import sqrt 
import numpy as np 
import matplotlib.pyplot as plt 

def d(P1,P2):
  return sqrt((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)

file = open('a280.tsp')
L_coord=[]
content = file.readlines()
for l in content[6:]:
  i=0
  for word in l.split():
    if i % 3 != 0:
      L_coord.append(float(word))
    i+=1

X_coord=[L_coord[i] for i in range(len(L_coord)) if i%2==0]
Y_coord=[L_coord[i] for i in range(len(L_coord)) if i%2!=0]

Coord_berlin = [[L_coord[i],L_coord[i+1]] for i in range(len(L_coord)-1,2)]

def plus_proche_voisin(pts,P):
  imin=0
  dmin = d(P,pts[0])
  for i in range(len(pts)):
    di=d(P,pts[i])
    if di < dmin:
      imin = i

def chemin_voyageur_ppv(pts):
  P=pts[0]
  pts_restants=pts[1:]
  L=[P]
  while len(pts_restants)>0:
    ppv = plus_proche_voisin(pts_restants,P)
    P=pts_restants[ppv]
    L.append(P)
    pts_restants = np.delete(pts_restants,[ppv],0)
  L.append(L[0])
  return L

pts = np.array(Coord_berlin)
start = time.time()

L_ppv = chemin_voyageur_ppv(pts)
distancef = 0
for i in range(len(L_ppv)-1):
  distance_f += d(L_ppv[i],L_ppv[i+1])
end = time.time()

print(end-start)

plt.scatter(X_coord,Y_coord,marker='o',s=15)
plt.plot([P[0] for P in L_ppv],[P[1] for P in L_ppv], c='b',linewidth=0.8)
plt.suptitle('Algo Glouton / plus proche voisin : Plus court chemin')
plt.title('pour une distance minimale de {}'.format(np.round(distancef,3)),fontsize=10)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()










