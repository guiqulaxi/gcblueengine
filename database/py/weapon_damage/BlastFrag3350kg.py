# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3350kg'
    dbObj.maxRange_m=7371.239746
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1205.799805
    dbObj.fragCharge_kg=1038.633423
    dbObj.radCharge_kg=120.579979
    dbObj.fragMetal_kg=1105.566772
    dbObj.fragFragment_kg=0.171459
    dbObj.fragSpread=0.300000
    return dbObj
