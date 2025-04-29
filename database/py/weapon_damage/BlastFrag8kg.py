# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag8kg'
    dbObj.maxRange_m=508.324371
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.828715
    dbObj.fragCharge_kg=2.514190
    dbObj.radCharge_kg=0.282871
    dbObj.fragMetal_kg=2.657095
    dbObj.fragFragment_kg=0.001107
    dbObj.fragSpread=0.300000
    return dbObj
