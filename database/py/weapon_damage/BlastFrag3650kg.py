# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3650kg'
    dbObj.maxRange_m=7614.581543
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1313.797729
    dbObj.fragCharge_kg=1131.634888
    dbObj.radCharge_kg=131.379776
    dbObj.fragMetal_kg=1204.567383
    dbObj.fragFragment_kg=0.184072
    dbObj.fragSpread=0.300000
    return dbObj
