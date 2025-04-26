# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-24750kT'
    dbObj.maxRange_m=83201.765625
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=27224999936.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=12375000064.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
