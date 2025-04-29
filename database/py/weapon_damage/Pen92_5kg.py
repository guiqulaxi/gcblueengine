# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen92.5kg'
    dbObj.maxRange_m=50.171139
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=64.750000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=9.250000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
