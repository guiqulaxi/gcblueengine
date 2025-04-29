# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag7.8kg'
    dbObj.maxRange_m=502.035553
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.757339
    dbObj.fragCharge_kg=2.451774
    dbObj.radCharge_kg=0.275734
    dbObj.fragMetal_kg=2.590887
    dbObj.fragFragment_kg=0.001087
    dbObj.fragSpread=0.300000
    return dbObj
