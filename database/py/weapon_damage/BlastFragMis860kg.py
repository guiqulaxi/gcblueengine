# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis860kg'
    dbObj.maxRange_m=6415.699707
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=114.684044
    dbObj.fragCharge_kg=422.343964
    dbObj.radCharge_kg=11.468405
    dbObj.fragMetal_kg=322.971985
    dbObj.fragFragment_kg=0.119531
    dbObj.fragSpread=0.300000
    return dbObj
