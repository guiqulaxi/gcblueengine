# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir19.5kg'
    dbObj.maxRange_m=2846.391602
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.421441
    dbObj.fragCharge_kg=8.362372
    dbObj.radCharge_kg=0.442144
    dbObj.fragMetal_kg=6.716187
    dbObj.fragFragment_kg=0.021948
    dbObj.fragSpread=0.180625
    return dbObj
