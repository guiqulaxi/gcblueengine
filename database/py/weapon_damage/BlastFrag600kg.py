# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag600kg'
    dbObj.maxRange_m=3698.573730
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=215.842239
    dbObj.fragCharge_kg=186.105179
    dbObj.radCharge_kg=21.584223
    dbObj.fragMetal_kg=198.052582
    dbObj.fragFragment_kg=0.039674
    dbObj.fragSpread=0.300000
    return dbObj
