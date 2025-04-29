# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2200kg'
    dbObj.maxRange_m=9225.404297
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=242.413696
    dbObj.fragCharge_kg=1114.390869
    dbObj.radCharge_kg=24.241369
    dbObj.fragMetal_kg=843.195435
    dbObj.fragFragment_kg=0.265406
    dbObj.fragSpread=0.300000
    return dbObj
