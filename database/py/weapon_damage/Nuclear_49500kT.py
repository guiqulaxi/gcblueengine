# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-49500kT'
    dbObj.maxRange_m=102433.390625
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=54449999872.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=24750000128.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
