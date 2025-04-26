# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast740kg'
    dbObj.maxRange_m=111.892967
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=720.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=72.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
