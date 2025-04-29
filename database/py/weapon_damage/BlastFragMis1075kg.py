# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1075kg'
    dbObj.maxRange_m=6903.068359
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=137.438904
    dbObj.fragCharge_kg=531.874084
    dbObj.radCharge_kg=13.743891
    dbObj.fragMetal_kg=405.687042
    dbObj.fragFragment_kg=0.140134
    dbObj.fragSpread=0.300000
    return dbObj
