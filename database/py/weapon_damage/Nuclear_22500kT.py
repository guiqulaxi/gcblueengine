# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-22500kT'
    dbObj.maxRange_m=80856.460938
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=24750000128.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=11249999872.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
