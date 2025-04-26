# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3.9kg'
    dbObj.maxRange_m=1593.666138
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.039093
    dbObj.fragCharge_kg=1.569271
    dbObj.radCharge_kg=0.103909
    dbObj.fragMetal_kg=1.291636
    dbObj.fragFragment_kg=0.007136
    dbObj.fragSpread=0.063196
    return dbObj
