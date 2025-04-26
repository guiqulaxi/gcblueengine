# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir4.7kg'
    dbObj.maxRange_m=1734.210938
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.230612
    dbObj.fragCharge_kg=1.905592
    dbObj.radCharge_kg=0.123061
    dbObj.fragMetal_kg=1.563796
    dbObj.fragFragment_kg=0.008363
    dbObj.fragSpread=0.067456
    return dbObj
