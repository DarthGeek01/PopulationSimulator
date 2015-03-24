__author__ = 'ariel'

from Organisms.OrganismThread import OrganismThread
from Crypto.Random import random

class OrganismManager(object):
    organisms = [OrganismThread]
    numYears = 0

    def __init__(self, organisms=None):
        if organisms != None:
            self.organisms = organisms

    def __addOrganism(self, organism):
        self.organisms.append(organism)

    def __doReproductionCycle(self):
        cycleGoing = True
        organismNumber = 0
        parentSample = self.__getOrganismsToReproduce()
        while cycleGoing:
            parent_one_local = parentSample[organismNumber]
            parent_two_local = parentSample[organismNumber + 1]
            self.organisms.append(OrganismThread(True, parent_one=parent_one_local, parent_two=parent_two_local))
            organismNumber += 2
            if organismNumber >= len(self.organisms):
                cycleGoing = False
            else:
                pass

    def __getOrganismsToReproduce(self):
         return  random.sample(self.organisms, (2 * int(((len(self.organisms) - 1) / 3))))

    def __populateOrganisms(self, numOrganisms):
        for i in range(numOrganisms):
            current = OrganismThread()
            current.makeTraitsRandom()
            self.organisms.append(current)

    def start(self):
        self.organisms = []
        yearsEnd = None
        initialOrganisms = None
        while True:
            try:
                yearsEnd = int(input("Enter number of years to simulate: "))
                break
            except ValueError:
                print("Not a number!")

        while True:
            try:
                initialOrganisms = int(input("Enter initial population size: "))
                break
            except ValueError:
                print("Not a number!")

        self.__populateOrganisms(initialOrganisms)

        while self.numYears <= yearsEnd:
            self.__doReproductionCycle()

        for organism in self.organisms:
            organism.printInfo()





