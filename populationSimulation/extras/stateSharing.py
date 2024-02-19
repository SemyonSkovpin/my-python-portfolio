import random
from matplotlib import pyplot as plt


'''
class Item():
    def __init__(self, state=bool(random.randint(0, 1)), change_prob=0,1):
        self.state = state
        self.change_prob = change_prob

    def challenge_state (self):
        if random.random() < self.change_prob:
            self.state = not self.state

    def get_state(self):
        return self.state
    

class group():
    def __init__(num_items=100, change_prob=0.125):
    
'''

change_prob = 0.125
state_a = 100
state_b = 900
state_a_log = [state_a]
timeSteps = 10000


for timeStep in range(timeSteps):
    print (timeStep)
    added_to_b = 0
    print(state_a, state_b)
    for i in range(state_a):
        if random.random() < change_prob:
            state_a -= 1
            added_to_b += 1
    for i in range(state_b):
        if random.random() < change_prob:
            state_b -= 1
            state_a += 1
    state_b += added_to_b
    if timeStep == 30:
        temp = state_a * 2 - 150
        state_b = state_a + state_b - temp
        state_a=temp
    if timeStep == 75:
        state_b = state_a + state_b
        state_a = 0
    state_a_log.append(state_a)

print('plot')
plt.figure('State tranfer')
plt.plot([i for i in range(timeSteps+1)], state_a_log, label='State-A')
plt.axhline(y=state_a+state_b, label='State-A + State-B', color='black')
plt.xlim(0, timeSteps)
plt.ylim(0, state_a+state_b+20)
plt.xlabel('Time steps')
plt.ylabel('Amount of items in State-A or State-B')
plt.legend()
plt.show()