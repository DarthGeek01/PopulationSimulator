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

from Genetics import Expressions, Genotypes
from Crypto.Random import random

class TraitAlleles(object):
    traitPhenotypes = {"furColor" : {"dominant" : "long", "recessive" : "short"},
                       "furLength" : {"dominant" : "black", "recessive" : "brown"},
                       "isTa" : {"dominant" : "tall", "recessive" : "short"}}

    traitIsComplete = False
    expression = None
    trait = None
    genotype = None
    phenotype = None
    letterOne = str
    letterTwo = str
    choices = []

    def __init__(self, trait, alleles=False, letter_one = None, letter_two = None):
        self.trait = trait

        if alleles:
            if letter_one != None:
                self.letterOne = letter_one
            if letter_two != None:
                self.letterTwo = letter_two
            if self.letterOne and self.letterTwo:
                if self.letterOne.isupper() and self.letterTwo.isupper():
                    self.expression = Expressions.HOMOZYGOUS_DOMINANT
                    self.genotype = Genotypes.DOMINANT
                elif self.letterOne.isupper() and not self.letterTwo.isupper():
                    self.expression = Expressions.HETEROZYGOUS_DOMINANT
                    self.genotype = Genotypes.DOMINANT
                elif not self.letterOne.isupper() and not self.letterTwo.isupper():
                    self.expression = Expressions.HOMOZYGOUS_RECESSIVE
                    self.genotype = Genotypes.RECESSIVE
                elif not self.letterOne.isupper() and self.letterTwo.isupper():
                    self.expression = Expressions.HETEROZYGOUS_DOMINANT
                    self.genotype = Genotypes.DOMINANT

            self.__determinePhenotype()

        if trait == "furColor":
            choices = list('Ff')
        elif trait == "furLength":
            choices = list('Ll')
        elif trait == "isTall":
            choices = list("Hh")

    def getGenotype(self):
        return self.genotype

    def getExpression(self):
        return self.expression

    def setLetterOne(self, letter):
        self.letterOne = letter

        if self.letterOne and self.letterTwo:
            if self.letterOne.isupper() and self.letterTwo.isupper():
                self.expression = Expressions.HOMOZYGOUS_DOMINANT
                self.genotype = Genotypes.DOMINANT
            elif self.letterOne.isupper() and not self.letterTwo.isupper():
                self.expression = Expressions.HETEROZYGOUS_DOMINANT
                self.genotype = Genotypes.DOMINANT
            elif not self.letterOne.isupper() and not self.letterTwo.isupper():
                self.expression = Expressions.HOMOZYGOUS_RECESSIVE
                self.genotype = Genotypes.RECESSIVE
            elif not self.letterOne.isupper() and self.letterTwo.isupper():
                self.expression = Expressions.HETEROZYGOUS_DOMINANT
                self.genotype = Genotypes.DOMINANT

            self.__determinePhenotype()

    def setLetterTwo(self, letter):
        self.letterTwo = letter

        if self.letterOne and self.letterTwo:
            if self.letterOne.isupper() and self.letterTwo.isupper():
                self.expression = Expressions.HOMOZYGOUS_DOMINANT
                self.genotype = Genotypes.DOMINANT
            elif self.letterOne.isupper() and not self.letterTwo.isupper():
                self.expression = Expressions.HETEROZYGOUS_DOMINANT
                self.genotype = Genotypes.DOMINANT
            elif not self.letterOne.isupper() and not self.letterTwo.isupper():
                self.expression = Expressions.HOMOZYGOUS_RECESSIVE
                self.genotype = Genotypes.RECESSIVE
            elif not self.letterOne.isupper() and self.letterTwo.isupper():
                self.expression = Expressions.HETEROZYGOUS_DOMINANT
                self.genotype = Genotypes.DOMINANT

            self.__determinePhenotype()

    def getRandomAllele(self):
        rand = random.randint(0, 1)
        if rand:
            return self.letterOne
        else:
            return self.letterTwo

    def __determinePhenotype(self):
        if self.genotype == Genotypes.DOMINANT:
            self.phenotype = self.traitPhenotypes[self.trait]["dominant"]
        else:
            self.genotype = self.traitPhenotypes[self.trait]["recessive"]

        self.choices = [self.letterOne, self.letterTwo]


    def populateWithRandom(self):
        self.letterOne = random.choice(self.choices)
        self.letterTwo = random.choice(self.choices)
        if self.letterOne.isupper() and self.letterTwo.isupper():
            self.expression = Expressions.HOMOZYGOUS_DOMINANT
            self.genotype = Genotypes.DOMINANT
        elif self.letterOne.isupper() and not self.letterTwo.isupper():
            self.expression = Expressions.HETEROZYGOUS_DOMINANT
            self.genotype = Genotypes.DOMINANT
        elif not self.letterOne.isupper() and not self.letterTwo.isupper():
            self.expression = Expressions.HOMOZYGOUS_RECESSIVE
            self.genotype = Genotypes.RECESSIVE
        elif not self.letterOne.isupper() and self.letterTwo.isupper():
            self.expression = Expressions.HETEROZYGOUS_DOMINANT
            self.genotype = Genotypes.DOMINANT

        self.__determinePhenotype()

    def getAlleles(self):
        if self.letterOne and self.letterTwo:
            return (self.letterOne, self.letterTwo)
        elif self.letterOne and not self.letterTwo:
            return self.letterOne
        elif self.letterTwo and not self.letterOne:
            return self.letterTwo

    def getAllelesAsList(self):
        return [self.letterOne, self.letterTwo]

    def getPhenotype(self):
        return self.phenotype