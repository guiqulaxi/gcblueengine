# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.4kg'
    dbObj.maxRange_m=124.805161
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.144000
    dbObj.fragCharge_kg=0.124000
    dbObj.radCharge_kg=0.014400
    dbObj.fragMetal_kg=0.132000
    dbObj.fragFragment_kg=0.000206
    dbObj.fragSpread=0.300000
    return dbObj
