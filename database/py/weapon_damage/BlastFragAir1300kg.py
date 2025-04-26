# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1300kg'
    dbObj.maxRange_m=7477.355957
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=160.112015
    dbObj.fragCharge_kg=647.258667
    dbObj.radCharge_kg=16.011202
    dbObj.fragMetal_kg=492.629333
    dbObj.fragFragment_kg=0.166880
    dbObj.fragSpread=0.300000
    return dbObj
