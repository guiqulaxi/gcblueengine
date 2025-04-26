# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag660kg'
    dbObj.maxRange_m=3849.712158
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=237.439880
    dbObj.fragCharge_kg=204.706741
    dbObj.radCharge_kg=23.743988
    dbObj.fragMetal_kg=217.853378
    dbObj.fragFragment_kg=0.043088
    dbObj.fragSpread=0.300000
    return dbObj
