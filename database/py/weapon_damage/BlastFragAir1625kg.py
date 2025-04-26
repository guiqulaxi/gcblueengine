# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1625kg'
    dbObj.maxRange_m=8192.517578
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=191.197006
    dbObj.fragCharge_kg=815.035339
    dbObj.radCharge_kg=19.119701
    dbObj.fragMetal_kg=618.767639
    dbObj.fragFragment_kg=0.204012
    dbObj.fragSpread=0.300000
    return dbObj
