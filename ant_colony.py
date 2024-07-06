import numpy as np
import matplotlib.pyplot as plt


def ant_colony_optimization(points, n_fourmis, n_iterations, alpha, beta, taux_evaporation, Q):
    n_points = len(points)
    pheromone = np.ones((n_points, n_points))
    meilleur_chemin = None
    dist_meilleur_chemin = np.inf

    for iteration in range(n_iterations):
        chemins = []
        dist_chemins = []

        for fourmi in range(n_fourmis):
            visite = [False]*n_points
            point_encours = np.random.randint(n_points)
            visite[point_encours] = True
            chemin = [point_encours]
            dist_chemin = 0

            while False in visite:
                pas_visite = np.where(np.logical_not(visite))[0]
                proba = np.zeros(len(pas_visite))

                for i, ppas_visite in enumerate(pas_visite):
                    proba[i] = pheromone[point_encours, ppas_visite]**alpha / distance(points[point_encours], points[ppas_visite])**beta

                proba /= np.sum(proba)

                prochain_point = np.random.choice(pas_visite, p=proba)
                chemin.append(prochain_point)
                dist_chemin += distance(points[point_encours], points[prochain_point])
                visite[prochain_point] = True
                point_encours = prochain_point

            chemin.append(chemin[0])
            dist_chemin += distance(points[0], points[chemin[-1]])
            chemins.append(chemin)
            dist_chemins.append(dist_chemin)

            if dist_chemin < dist_meilleur_chemin:
                meilleur_chemin = chemin
                dist_meilleur_chemin = dist_chemin

        pheromone *= (1-taux_evaporation)

        for chemin, dist_chemin in zip(chemins, dist_chemins):# cree un couple du chemin et de sa longueur
            for i in range(n_points-1):
                pheromone[chemin[i], chemin[i+1]] += Q/dist_chemin
            pheromone[chemin[-1], chemin[0]] += Q/dist_chemin

    dist_meilleur_chemin += distance(points[0], points[chemin[-1]])
    return meilleur_chemin, dist_meilleur_chemin

# Assuming 'cities' is defined elsewhere in the code

L = []
for i in np.arange(0.1,1,0.1):
    L.append(ant_colony_optimization(cities, n_fourmis=100, n_iterations=100, alpha=1, beta=3, taux_evaporation=i, Q=100)[1])
plt.plot([i for i in np.arange(0.1,1,0.1)], L)

Q = [i for i in range(1,100,10)]
rho1 = [ant_colony_optimization(cities, taux_evaporation=0.6, Q=i, n_fourmis=50, n_iterations=100, alpha=1, beta=4)[1] for i in range(1,100,10)]
rho2 = [ant_colony_optimization(cities, taux_evaporation=0.3, Q=i, n_fourmis=50, n_iterations=100, alpha=1, beta=4)[1] for i in range(1,100,10)]

plt.plot(Q, rho1, 'b:s', label='Rho=0.3')
plt.plot(Q, rho2, 'g:s', label='Rho=0.6')
plt.title('valeur du chemin trouvée pour diférentes valeurs de Q', fontsize = 10)
plt.xlabel('Q')
plt.ylabel('temps')
plt.show()

chemin, length = ant_colony_optimization(cities, n_fourmis=50, n_iterations=100, alpha=1, beta=4, taux_evaporation=0.5, Q=100)

plt.scatter([cities[i][0] for i in range(0,len(chemin)-1)], [cities[i][1] for i in range(0,len(chemin)-1)], marker='o', s = 15)
# Plot le chemin.
plt.plot([cities[chemin[i]][0] for i in range(0,len(chemin))], [cities[chemin[i]][1] for i in range(0,len(chemin))], c='r', linewidth=0.8, linestyle="--")

ant_distance = sum(distance(cities[chemin[i]], cities[chemin[i + 1]]) for i in range(len(chemin) - 1))
plt.suptitle('Algo colonie fourmis : Plus court chemin')
plt.title('Pour une distance minimale de {}'.format(np.round(ant_distance,3)), fontsize = 10)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()
