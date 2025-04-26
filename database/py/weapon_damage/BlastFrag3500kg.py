# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3500kg'
    dbObj.maxRange_m=7495.053711
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1259.798706
    dbObj.fragCharge_kg=1085.134155
    dbObj.radCharge_kg=125.979874
    dbObj.fragMetal_kg=1155.067139
    dbObj.fragFragment_kg=0.177812
    dbObj.fragSpread=0.300000
    return dbObj
