import random
from math import exp
import GA_operatorsT
class chromosome:
    def __init__(self,length=8):
        self.genes=[None]*length
        for i in range(length):
            self.genes[i]=random.choice([0,1])
        self.evaluate()



    def evaluate(self):
        x_value=(4*self.genes[1]+2*self.genes[2]+1*self.genes[3])
        if x_value.genes[0]:
            x_value*=-1
        y_value=(4*self.genes[-3]+2*self.genes[-2]+1*self.genes[-1])
        if y_value.genes[-4]:
            y_value*=-1


        value1=-1*(pow(x_value,2)+pow(y_value,2))
        value2=-1*(pow(x_value-1.7,2)+pow(y_value-1.7,2))
        self.fitness=(exp(value1)+(2*exp(value2)))
class selection:

    def binary_tor(pop,return_pop,T_size):
        new_population=[]
        for i in range(return_pop):
            Tour_teams=[]
            for j in range(T_size):
                Tour_teams.append(random.choice(pop))
            new_population.append(max(Tour_teams,key=lambda X:X.fitness))
            
        return (new_population)
class operator:
    def crossover(parent1,parent2):
        child1=copy.deepcopy(parent1)
        child2=copy.deepcopy(parent2)

        crosspoint=random.randint(0,len(parent1))
        child1[crosspoint:]=parent1.genes[crosspoint:]
        child2[crosspoint:]=parent2.genes[crosspoint:]

        child1.evaluate()
        child2.evaluate()
        return child1,child2


pop=[_ for _ in range(10)]
for i in range(0,10):
    pop[i]=GA_operatorsT.chromosome(8)
    print(pop.genes[i],pop.ftness[i])
