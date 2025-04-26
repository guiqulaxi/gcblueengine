# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-27500kT'
    dbObj.maxRange_m=85873.625000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=30250000384.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=13749999616.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
