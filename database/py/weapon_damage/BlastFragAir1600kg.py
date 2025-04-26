# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1600kg'
    dbObj.maxRange_m=8141.213379
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=188.867325
    dbObj.fragCharge_kg=802.088440
    dbObj.radCharge_kg=18.886732
    dbObj.fragMetal_kg=609.044250
    dbObj.fragFragment_kg=0.201204
    dbObj.fragSpread=0.300000
    return dbObj
