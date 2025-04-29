# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag26.5kg'
    dbObj.maxRange_m=916.919312
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.459176
    dbObj.fragCharge_kg=8.268883
    dbObj.radCharge_kg=0.945918
    dbObj.fragMetal_kg=8.771941
    dbObj.fragFragment_kg=0.002841
    dbObj.fragSpread=0.300000
    return dbObj
