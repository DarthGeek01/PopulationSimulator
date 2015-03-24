__author__ = 'ariel'
"""
    Python Population Simulator
    Copyright (C) 2015  Ariel Young

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

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