# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-32500kT'
    dbObj.maxRange_m=90286.953125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=35749998592.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=16250000384.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
