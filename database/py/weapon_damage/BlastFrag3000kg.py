# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3000kg'
    dbObj.maxRange_m=7063.894043
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1079.802490
    dbObj.fragCharge_kg=930.131653
    dbObj.radCharge_kg=107.980255
    dbObj.fragMetal_kg=990.065796
    dbObj.fragFragment_kg=0.156260
    dbObj.fragSpread=0.300000
    return dbObj
