# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir900kg'
    dbObj.maxRange_m=6499.539062
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=119.009071
    dbObj.fragCharge_kg=442.660614
    dbObj.radCharge_kg=11.900908
    dbObj.fragMetal_kg=338.330322
    dbObj.fragFragment_kg=0.122940
    dbObj.fragSpread=0.300000
    return dbObj
