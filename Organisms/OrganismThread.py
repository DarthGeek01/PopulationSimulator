__author__ = 'ariel'

from threading import Thread
from Genetics.Allele import TraitAlleles
from Genetics import Expressions
from Crypto.Random import random

class OrganismThread(Thread):
    traitList = {"furColor" : TraitAlleles(trait='furColor'), "furLength" : TraitAlleles(trait='furLength'), "isTall" : TraitAlleles(trait='isTall')}

    def __init__(self, parents = False, parent_one = None, parent_two = None):
        if parents:
            for key in self.traitList.keys():
                self.traitList[key] = TraitAlleles(parent_one.getRandomAllele(), parent_two.getRandomAllele())


    def getRandomAllele(self, trait):
        return self.traitList[trait].getRandomAllele()

    def makeTraitsRandom(self):
        for key in self.traitList.keys():
            self.traitList[key].populateWithRandom()

    def printInfo(self):
        print("Trait Genotypes:")
        print("\tFur Color: %s%s" % self.traitList['furColor'].getAlleles())
        print("\tFur Length: %s%s" % self.traitList['furLength'].getAlleles())
        print("\tHeight: %s%s" % self.traitList['isTall'].getAlleles())
        print("\nTrait Phenotypes: ")
        print("\tFur Color: %s%s" % self.traitList['furColor'].getPhenotype())
        print("\tFur Length: %s%s" % self.traitList['furLength'].getPhenotype())
        print("\tHeight: %s%s \n\n" % self.traitList['isTall'].getPhenotype())