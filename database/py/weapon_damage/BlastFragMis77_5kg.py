# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis77.5kg'
    dbObj.maxRange_m=3774.687500
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=14.934943
    dbObj.fragCharge_kg=34.993370
    dbObj.radCharge_kg=1.493494
    dbObj.fragMetal_kg=27.571686
    dbObj.fragFragment_kg=0.038943
    dbObj.fragSpread=0.300000
    return dbObj
