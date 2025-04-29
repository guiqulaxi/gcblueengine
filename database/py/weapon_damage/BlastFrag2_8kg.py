# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.8kg'
    dbObj.maxRange_m=292.524200
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.982606
    dbObj.fragCharge_kg=0.884929
    dbObj.radCharge_kg=0.098261
    dbObj.fragMetal_kg=0.932465
    dbObj.fragFragment_kg=0.000516
    dbObj.fragSpread=0.300000
    return dbObj
