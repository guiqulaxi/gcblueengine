# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir55kg'
    dbObj.maxRange_m=3509.339844
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=11.064185
    dbObj.fragCharge_kg=24.523876
    dbObj.radCharge_kg=1.106418
    dbObj.fragMetal_kg=19.411938
    dbObj.fragFragment_kg=0.033527
    dbObj.fragSpread=0.300000
    return dbObj
