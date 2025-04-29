# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='1lb bomblet'
    dbObj.maxRange_m=65.653557
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.045360
    dbObj.fragCharge_kg=0.204120
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=0.204120
    dbObj.fragFragment_kg=0.000340
    dbObj.fragSpread=1.000000
    return dbObj
