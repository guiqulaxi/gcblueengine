# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis82.5kg'
    dbObj.maxRange_m=3798.744873
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=15.771277
    dbObj.fragCharge_kg=37.335815
    dbObj.radCharge_kg=1.577128
    dbObj.fragMetal_kg=29.392908
    dbObj.fragFragment_kg=0.039454
    dbObj.fragSpread=0.300000
    return dbObj
