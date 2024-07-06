import numpy as np
import matplotlib.pyplot as plt

#Algo 2-opt
def distance(pt1, pt2):    #calcule la distance entre 2 points
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]
    
    distance = np.sqrt(dx*dx + dy*dy)
    
    return distance

def algo2opt(points):
    """Algorithme 2-opt"""
    nb_points = len(points)
    chemin = [i for i in range(nb_points)]
    chemin.append(0)
    meilleur_chemin = chemin
    amelioration = True
    
    while amelioration:
        amelioration = False
        for i in range(1, nb_points +1):
            for j in range(i + 1, nb_points+1):
                if j - i == 1:
                    continue  # Ignore les échanges adjacents
                nouveau_chemin = chemin[:i] + chemin[i:j][::-1] + chemin[j:]
                if distance(points[chemin[i-1]], points[chemin[i]]) + distance(points[chemin[j-1]], points[chemin[j]]) > distance(points[nouveau_chemin[i-1]], points[nouveau_chemin[i]]) + distance(points[nouveau_chemin[j-1]], points[nouveau_chemin[j]]):
                    chemin = nouveau_chemin
                    amelioration = True
        if chemin == meilleur_chemin:
            break
        meilleur_chemin = chemin
    return chemin

# Assuming 'cities' is defined elsewhere in the code
chemin = algo2opt(cities)

# Plot les villes.
plt.scatter([cities[i][0] for i in range(0,len(chemin)-1)], [cities[i][1] for i in range(0,len(chemin)-1)], marker='o', s = 15)

# Plot le chemin.
plt.plot([cities[chemin[i]][0] for i in range(0,len(chemin))], [cities[chemin[i]][1] for i in range(0,len(chemin))], c='r', linewidth=0.8, linestyle='--')

opt2_distance = sum(distance(cities[chemin[i]], cities[chemin[i + 1]]) for i in range(len(chemin) - 1))
plt.suptitle('Algo 2-opt : Plus court chemin')
plt.title('Pour une distance minimale de {}'.format(np.round(opt2_distance,3)), fontsize = 10)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()
