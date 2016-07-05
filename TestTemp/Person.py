# -*- coding:utf-8 -*-
__author__ = 'pzk'


class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        print("initializing %s" % self.name)
        Person.population += 1

    def __del__(self):
        print("%s say bye" % self.name)
        Person.population -= 1
        if Person.population == 0:
            print ("I'm the last one")
        else:
            print ("There are still %d person left" % Person.population)

    def SayHi(self):
        print ("Hi,my name is %s" % self.name)

    def HowMany(self):
        if Person.population == 1:
            print("I am the only Person here")
        else:
            print ("We have %d person here" % Person.population)

    def Invoke(self):
        print("ok")


swaroop = Person("Swaroop")  # initializing Swaroop
swaroop.SayHi()  # Hi,my name is Swaroop
swaroop.HowMany()  # I am the only Person here

kalam = Person("Kalam")  # initializing Kalam
kalam.SayHi()  # Hi,my name is Kalam
kalam.HowMany()  # We have 2 person here

swaroop.SayHi()  # Hi,my name is Swaroop
swaroop.HowMany()  # We have 2 person here

kalam.Invoke()  # ok
# Kalam say bye
# There are still 1 person left
# Swaroop say bye
# I'm the last one
