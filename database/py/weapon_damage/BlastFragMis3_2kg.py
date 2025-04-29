# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3.2kg'
    dbObj.maxRange_m=1454.713745
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.868202
    dbObj.fragCharge_kg=1.277199
    dbObj.radCharge_kg=0.086820
    dbObj.fragMetal_kg=1.054599
    dbObj.fragFragment_kg=0.006026
    dbObj.fragSpread=0.059076
    return dbObj
