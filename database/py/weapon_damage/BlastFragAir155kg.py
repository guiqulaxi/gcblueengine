# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir155kg'
    dbObj.maxRange_m=4202.677734
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=27.220144
    dbObj.fragCharge_kg=71.753235
    dbObj.radCharge_kg=2.722014
    dbObj.fragMetal_kg=56.026619
    dbObj.fragFragment_kg=0.048634
    dbObj.fragSpread=0.300000
    return dbObj
