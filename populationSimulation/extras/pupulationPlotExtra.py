from matplotlib import pyplot as plt

initialPop = 1
maxPopulation = 10000               
growthRate = 0.01
timeSteps = 10000
populationTrack = []


for i in range(timeSteps):
    last = populationTrack[-1] if len(populationTrack)!=0 else initialPop
    populationTrack.append(last + last * growthRate * (1 - last / maxPopulation))

exponent = [(1 + growthRate)**timeStep for timeStep in range(timeSteps)]

plt.figure('Population over time')
plt.plot([i for i in range(timeSteps)], exponent, label = 'exponent')
plt.plot([i for i in range(timeSteps)], populationTrack, label = 'change in population')
plt.plot([i for i in range(timeSteps)], [maxPopulation for i in range(timeSteps)], label='max population',    color='black')
plt.xlim(0, timeSteps)
plt.ylim(0, 10000)
plt.xlabel = 'time steps'
plt.ylabel = 'population'
plt.legend()
plt.show()



