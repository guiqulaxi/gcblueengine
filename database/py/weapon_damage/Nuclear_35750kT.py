# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-35750kT'
    dbObj.maxRange_m=92905.796875
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=39324999680.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=17874999296.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
