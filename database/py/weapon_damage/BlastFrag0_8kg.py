# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.8kg'
    dbObj.maxRange_m=155.612900
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.288000
    dbObj.fragCharge_kg=0.248000
    dbObj.radCharge_kg=0.028800
    dbObj.fragMetal_kg=0.264000
    dbObj.fragFragment_kg=0.000254
    dbObj.fragSpread=0.300000
    return dbObj
