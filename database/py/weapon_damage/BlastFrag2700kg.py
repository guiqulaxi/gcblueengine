# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2700kg'
    dbObj.maxRange_m=6776.963379
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=971.805115
    dbObj.fragCharge_kg=837.129883
    dbObj.radCharge_kg=97.180511
    dbObj.fragMetal_kg=891.064941
    dbObj.fragFragment_kg=0.142799
    dbObj.fragSpread=0.300000
    return dbObj
