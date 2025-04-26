# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1325kg'
    dbObj.maxRange_m=7537.027832
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=162.568634
    dbObj.fragCharge_kg=660.120911
    dbObj.radCharge_kg=16.256863
    dbObj.fragMetal_kg=502.310455
    dbObj.fragFragment_kg=0.169814
    dbObj.fragSpread=0.300000
    return dbObj
