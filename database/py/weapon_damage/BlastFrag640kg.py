# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag640kg'
    dbObj.maxRange_m=3804.440430
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=230.240646
    dbObj.fragCharge_kg=198.506241
    dbObj.radCharge_kg=23.024063
    dbObj.fragMetal_kg=211.253113
    dbObj.fragFragment_kg=0.042049
    dbObj.fragSpread=0.300000
    return dbObj
