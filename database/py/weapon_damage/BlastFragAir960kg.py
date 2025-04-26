# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir960kg'
    dbObj.maxRange_m=6617.677734
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=125.414963
    dbObj.fragCharge_kg=473.190033
    dbObj.radCharge_kg=12.541496
    dbObj.fragMetal_kg=361.395020
    dbObj.fragFragment_kg=0.127837
    dbObj.fragSpread=0.300000
    return dbObj
