# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag280kg'
    dbObj.maxRange_m=2696.740967
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=100.661026
    dbObj.fragCharge_kg=86.892647
    dbObj.radCharge_kg=10.066103
    dbObj.fragMetal_kg=92.446327
    dbObj.fragFragment_kg=0.020934
    dbObj.fragSpread=0.300000
    return dbObj
