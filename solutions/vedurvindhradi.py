
wind = {
    "Logn" : (0, 0.2),
    "Andvari" : (0.3, 1.5),
    "Kul" : (1.6, 3.3),
    "Gola" : (3.4, 5.4),
    "Stinningsgola" : (5.5, 7.9),
    "Kaldi" : (8.0, 10.7),
    "Stinningskaldi" : (10.8, 13.8),
    "Allhvass vindur" : (13.9, 17.1),
    "Hvassvidri" : (17.2, 20.7),
    "Stormur" : (20.8, 24.4),
    "Rok" : (24.5, 28.4),
    "Ofsavedur" : (28.5, 32.6),
    "Farvidri" : (32.7, float('inf'))
}

n = float(input())

for k, v in wind.items():
    if v[0] <= n <= v[1]:
        print(k)

