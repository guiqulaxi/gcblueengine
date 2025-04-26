# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-580kT'
    dbObj.maxRange_m=26982.884766
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=638000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=290000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
