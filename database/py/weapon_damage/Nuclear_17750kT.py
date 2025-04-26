# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-17750kT'
    dbObj.maxRange_m=75304.250000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=19524999168.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=8874999808.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
