# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-33000kT'
    dbObj.maxRange_m=90701.437500
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=36300001280.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=16499999744.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
