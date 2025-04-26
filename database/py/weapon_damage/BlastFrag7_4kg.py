# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag7.4kg'
    dbObj.maxRange_m=489.013916
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.614637
    dbObj.fragCharge_kg=2.326908
    dbObj.radCharge_kg=0.261464
    dbObj.fragMetal_kg=2.458454
    dbObj.fragFragment_kg=0.001045
    dbObj.fragSpread=0.300000
    return dbObj
