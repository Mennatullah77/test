# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:07:44 2021

@author: A
"""
import matplotlib.pyplot as plt
# Exercise #3: Design Car Movement 
import random
import matplotlib as plt
class car():
    def __init__(self, movingstarttime , maxspeed ,currentspeed = 0 ):
        self.ismoving = False
        self.movingstarttime = movingstarttime
        self.accvalue = 5
        self.decvalue = -1.5
        self.maxspeed = maxspeed
        self.currentspeed = currentspeed
        self.timerequiredtobreak = 0
    def startmoving(self , t):
        if self.movingstarttime >= t:
            self.ismoving = True
    def accelerate(self ):
        if(self.ismoving):
            if (self.currentspeed  < self.maxspeed):
                self.currentspeed += self.accvalue
            else:
                self.currentspeed = self.maxspeed
    def daccelerate(self ):
        if(self.ismoving):
            if (self.currentspeed + self.decvalue > 0):
                self.currentspeed += self.decvalue
            else:
                self.currentspeed = 0
    def checkthespeed(self):
        if self.currentspeed > self.maxspeed:
            print("The maxspeed limit is excceeded!!!")
        else:
            print("you havn't exceeded the max speed yet") 
    def carbreak(self ):
        self.timerequiredtobreak = (0-self.currentspeed)/ -3.4
        self.currentspeed = 0
        return self.timerequiredtobreak             
    def resumemoving(self , t):
        if(self.movingstarttime < t):
            if self.currentspeed == 0:
                self.currentspeed += self.accvalue 
                return True
runtime = 20  
movingstarttime = random.randint(0 , 5) 
maxspeed = random.randint(90 , 120)
breaktime = random.randint(10 , runtime)
time_to_change_from_acc_to_dec = random.randint(3 , 5)
print(movingstarttime , maxspeed , time_to_change_from_acc_to_dec, breaktime)
car1 = car(movingstarttime ,  maxspeed)
i = 0
flag = 'acc'
distance = 0
while i <= runtime: 
    car1.startmoving(i)
    if car1.resumemoving(i):
        flag = 'acc'
    if i % time_to_change_from_acc_to_dec == 0:
        if flag == 'acc':
            flag = 'dec'
        else:
            flag = 'acc' 
    if flag == 'acc':
        car1.accelerate()
        distance = car1.currentspeed * i + 0.5 * i**2 * car1.accvalue
    else:
        car1.daccelerate()
        distance += car1.currentspeed  + 0.5 * i * car1.decvalue
    car1.checkthespeed()
    if(i == 12):
        i += car1.carbreak()
    
    distance = .5*(car1.accvalue)*(i**2)
    print(car1.currentspeed , flag , maxspeed , distance )
    f = open('Cardata' , 'a')
    f.write('at time = '+ str(i) + ' second: \n' +'Currentspeed: ' + str(car1.currentspeed) +', acc/dec: ' + flag + ', maxspeed: ' + str(maxspeed) +', distance travelled: '+ str(distance) +'\n')
    f = open('Cardata' , 'r')
    print(f.read())
    i += 1

    



