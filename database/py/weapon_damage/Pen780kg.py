# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen780kg'
    dbObj.maxRange_m=102.046059
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=546.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=78.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
