# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1050kg'
    dbObj.maxRange_m=4657.435547
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=377.828430
    dbObj.fragCharge_kg=325.614380
    dbObj.radCharge_kg=37.782845
    dbObj.fragMetal_kg=346.557190
    dbObj.fragFragment_kg=0.064082
    dbObj.fragSpread=0.300000
    return dbObj
