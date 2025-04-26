# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2850kg'
    dbObj.maxRange_m=10156.908203
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=295.840637
    dbObj.fragCharge_kg=1455.772949
    dbObj.radCharge_kg=29.584063
    dbObj.fragMetal_kg=1098.386475
    dbObj.fragFragment_kg=0.328957
    dbObj.fragSpread=0.300000
    return dbObj
