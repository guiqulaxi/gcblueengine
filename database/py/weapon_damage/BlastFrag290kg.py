# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag290kg'
    dbObj.maxRange_m=2734.740967
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=104.260162
    dbObj.fragCharge_kg=89.993225
    dbObj.radCharge_kg=10.426017
    dbObj.fragMetal_kg=95.746613
    dbObj.fragFragment_kg=0.021526
    dbObj.fragSpread=0.300000
    return dbObj
