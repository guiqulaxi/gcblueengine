# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis24kg'
    dbObj.maxRange_m=2993.749268
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.318869
    dbObj.fragCharge_kg=10.374087
    dbObj.radCharge_kg=0.531887
    dbObj.fragMetal_kg=8.307044
    dbObj.fragFragment_kg=0.024290
    dbObj.fragSpread=0.225625
    return dbObj
