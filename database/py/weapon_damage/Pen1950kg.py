# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1950kg'
    dbObj.maxRange_m=138.455521
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1365.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=195.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
