# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag6.4kg'
    dbObj.maxRange_m=453.559814
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.258218
    dbObj.fragCharge_kg=2.014521
    dbObj.radCharge_kg=0.225822
    dbObj.fragMetal_kg=2.127261
    dbObj.fragFragment_kg=0.000936
    dbObj.fragSpread=0.300000
    return dbObj
