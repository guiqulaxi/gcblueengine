# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag77.5kg'
    dbObj.maxRange_m=1516.054688
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=27.792709
    dbObj.fragCharge_kg=24.096527
    dbObj.radCharge_kg=2.779271
    dbObj.fragMetal_kg=25.610764
    dbObj.fragFragment_kg=0.006929
    dbObj.fragSpread=0.300000
    return dbObj
