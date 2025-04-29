# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir255kg'
    dbObj.maxRange_m=4529.914551
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=41.650585
    dbObj.fragCharge_kg=120.132942
    dbObj.radCharge_kg=4.165059
    dbObj.fragMetal_kg=93.216469
    dbObj.fragFragment_kg=0.056874
    dbObj.fragSpread=0.300000
    return dbObj
