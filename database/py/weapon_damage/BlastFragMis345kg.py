# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis345kg'
    dbObj.maxRange_m=4934.299316
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=53.778759
    dbObj.fragCharge_kg=164.247498
    dbObj.radCharge_kg=5.377876
    dbObj.fragMetal_kg=126.973747
    dbObj.fragFragment_kg=0.068119
    dbObj.fragSpread=0.300000
    return dbObj
