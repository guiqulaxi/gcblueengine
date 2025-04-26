# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag17kg'
    dbObj.maxRange_m=747.813904
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.050124
    dbObj.fragCharge_kg=5.316584
    dbObj.radCharge_kg=0.605012
    dbObj.fragMetal_kg=5.633292
    dbObj.fragFragment_kg=0.002023
    dbObj.fragSpread=0.300000
    return dbObj
