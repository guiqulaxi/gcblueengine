# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='76mm HE-MOM 0.8 FRAG'
    dbObj.maxRange_m=75.659332
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.080000
    dbObj.fragCharge_kg=0.400000
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=0.400000
    dbObj.fragFragment_kg=0.010000
    dbObj.fragSpread=0.500000
    return dbObj
