# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag650kg'
    dbObj.maxRange_m=3827.225830
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=233.840256
    dbObj.fragCharge_kg=201.606491
    dbObj.radCharge_kg=23.384026
    dbObj.fragMetal_kg=214.553253
    dbObj.fragFragment_kg=0.042570
    dbObj.fragSpread=0.300000
    return dbObj
