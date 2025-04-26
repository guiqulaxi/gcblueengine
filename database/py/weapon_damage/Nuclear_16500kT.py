# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-16500kT'
    dbObj.maxRange_m=73672.460938
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=18150000640.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=8249999872.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
