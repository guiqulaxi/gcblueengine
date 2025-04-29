# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3050kg'
    dbObj.maxRange_m=7109.500000
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1097.802124
    dbObj.fragCharge_kg=945.631897
    dbObj.radCharge_kg=109.780212
    dbObj.fragMetal_kg=1006.565979
    dbObj.fragFragment_kg=0.158464
    dbObj.fragSpread=0.300000
    return dbObj
