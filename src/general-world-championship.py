import matplotlib.pyplot as plt
from datetime import datetime

motoGpGrandPrix = ['QAT', 'INA', 'ARG', 'USA', 'POR', 'ESP', 'FRA', 'ITA', 'ESP', 'GER', 'NED', 'FIN', 'GBR', 'AUT', 'ITA', 'ESP', 'JPN', 'THA', 'AUS', 'MAS', 'ESP']

motoGP_riders = {
                            #   QAT     INA     ARG     USA     POR     ESP     FRA     ITA     ESP     GER     NED     FIN     GBR     AUT     ITA     ESP     JPN     THA     AUS     MAS     ESP
    'Aleix Espargaro':       [  13,     7,      25,     5,      16,     16,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Alex Marquez':          [  0,      3,      1,      0,      9,      3,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],  
    'Alex Rins':             [  9,      11,     16,     20,     13,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Andrea Dovizioso':      [  2,      0,      0,      0,      5,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Brad Binder':           [  20,     8,      10,     4,      0,      6,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Darryn Binder':         [  0,      6,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Enea Bastianini':       [  25,     5,      6,      25,     0,      8,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Fabio Di Giannantonio': [  0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Fabio Quartararo':      [  7,      20,     8,      9,      25,     20,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Francesco Bagnaia':     [  0,      1,      11,     11,     8,      25,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Franco Morbidelli':     [  5,      9,      0,      1,      3,      1,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Jack Miller':           [  0,      13,     2,      16,     0,      11,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Joan Mir':              [  10,     10,     13,     13,     0,      10,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Johann Zarco':          [  8,      16,     0,      7,      20,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Jorge Martin':          [  0,      0,      20,     8,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Lorenzo Savadori':      [  0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Luca Marini':           [  3,      2,      5,      0,      4,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Marc Marquez':          [  11,     0,      0,      10,     10,     13,     0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Marco Bezzecchi':       [  0,      0,      7,      0,      1,      7,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Maverick Viñales':      [  4,      0,      9,      6,      6,      2,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Miguel Oliveira':       [  0,      25,     3,      0,      11,     4,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Pol Espargaro':         [  16,     4,      0,      3,      7,      5,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Raul Fernandez':        [  0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Remy Gardner':          [  1,      0,      0,      0,      2,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Stefan Bradl':          [  0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    'Takaaki Nakagami':      [  6,      0,      4,      2,      0,      9,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0]
}

# Get time
now = datetime.now()

# Get rider and total points.
motoGpGeneral = {x:sum(motoGP_riders[x]) for x in motoGP_riders}

# Sorted rider by total points.
motoGpGeneral = {k: v for k, v in sorted(motoGpGeneral.items(), key=lambda item: item[1], reverse=True)}

# Get X and Y data.
X_riders = list(motoGpGeneral.keys())
Y_points = list(motoGpGeneral.values())

# Create the general plot.
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(26,8), dpi=600)
fig.suptitle(('MotoGP World Champion Ship Evolution - Author: @JaviKarra94 | Generation day: ' + now.strftime("%d-%m-%y")), fontsize=15)

# Create subplot classification.
axs[0].barh(X_riders, Y_points)
axs[0].set_ylabel('Moto Gp - Riders', fontsize=15)
axs[0].set_xlabel('General World Championship points', fontsize=15)

for i in range(len(X_riders)):
    if (i != 0):
        axs[0].text(x=int(Y_points[i]) + 1, 
                    y=X_riders[i], 
                    s=(str(Y_points[i]) + ' (' + str(Y_points[i] - Y_points[0]) +')'), 
                    fontsize=12, 
                    verticalalignment='center')
    else:
        axs[0].text(x=int(Y_points[i]) + 1, 
                    y=X_riders[i], 
                    s=Y_points[i], 
                    fontsize=12, 
                    verticalalignment='center')

# Create plot top 'n' classification evolution.
nTopRiders = 6 
nGrandPrix = 6

for item in list(motoGpGeneral.keys())[:nTopRiders]:

    riderEvolution = []

    for i in range(len(list(motoGP_riders[item]))):
        
        if(i + 1 < len(list(motoGP_riders[item]))):
            riderEvolution.append(sum(list(motoGP_riders[item])[0:i+1]))
        else:
            riderEvolution.append(sum(list(motoGP_riders[item])))

    axs[1].plot(motoGpGrandPrix[:nGrandPrix], riderEvolution[:nGrandPrix])
    axs[1].legend(list(motoGpGeneral.keys())[:nTopRiders])
    axs[1].grid(True)
    axs[1].set_ylabel(('General World Championship points: Top ' + str(nTopRiders) + ' Moto GP Riders'), fontsize=15)
    axs[1].set_xlabel('World Championship Grand Prix', fontsize=15)

# Save figure
fig.tight_layout()
fig.savefig(".\images\MotoGpGeneralClassification.png")