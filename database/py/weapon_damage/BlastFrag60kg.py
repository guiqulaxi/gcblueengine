# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag60kg'
    dbObj.maxRange_m=1340.645752
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=21.499022
    dbObj.fragCharge_kg=18.667320
    dbObj.radCharge_kg=2.149902
    dbObj.fragMetal_kg=19.833660
    dbObj.fragFragment_kg=0.005534
    dbObj.fragSpread=0.300000
    return dbObj
