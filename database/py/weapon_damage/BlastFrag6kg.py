# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag6kg'
    dbObj.maxRange_m=438.052765
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.115810
    dbObj.fragCharge_kg=1.889460
    dbObj.radCharge_kg=0.211581
    dbObj.fragMetal_kg=1.994730
    dbObj.fragFragment_kg=0.000891
    dbObj.fragSpread=0.300000
    return dbObj
