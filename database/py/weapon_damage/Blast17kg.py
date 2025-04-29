# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast17kg'
    dbObj.maxRange_m=32.140350
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=17.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1.700000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
