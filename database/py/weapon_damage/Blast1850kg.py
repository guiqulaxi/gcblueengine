# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1850kg'
    dbObj.maxRange_m=153.207245
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1850.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=185.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
