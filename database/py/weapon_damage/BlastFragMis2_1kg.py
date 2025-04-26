# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2.1kg'
    dbObj.maxRange_m=1180.060059
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.591573
    dbObj.fragCharge_kg=0.823618
    dbObj.radCharge_kg=0.059157
    dbObj.fragMetal_kg=0.684809
    dbObj.fragFragment_kg=0.004125
    dbObj.fragSpread=0.053156
    return dbObj
