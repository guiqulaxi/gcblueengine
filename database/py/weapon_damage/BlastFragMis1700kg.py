# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1700kg'
    dbObj.maxRange_m=8341.716797
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=198.129715
    dbObj.fragCharge_kg=853.913513
    dbObj.radCharge_kg=19.812971
    dbObj.fragMetal_kg=647.956787
    dbObj.fragFragment_kg=0.212306
    dbObj.fragSpread=0.300000
    return dbObj
