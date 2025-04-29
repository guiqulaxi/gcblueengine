# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag185kg'
    dbObj.maxRange_m=2265.741211
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=66.471252
    dbObj.fragCharge_kg=57.435833
    dbObj.radCharge_kg=6.647125
    dbObj.fragMetal_kg=61.092918
    dbObj.fragFragment_kg=0.014857
    dbObj.fragSpread=0.300000
    return dbObj
