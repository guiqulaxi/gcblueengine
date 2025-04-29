# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.3kg'
    dbObj.maxRange_m=113.861015
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.108000
    dbObj.fragCharge_kg=0.093000
    dbObj.radCharge_kg=0.010800
    dbObj.fragMetal_kg=0.099000
    dbObj.fragFragment_kg=0.000190
    dbObj.fragSpread=0.300000
    return dbObj
