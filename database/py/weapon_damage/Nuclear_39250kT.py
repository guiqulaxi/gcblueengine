# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-39250kT'
    dbObj.maxRange_m=95545.867188
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=43174998016.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=19625000960.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
