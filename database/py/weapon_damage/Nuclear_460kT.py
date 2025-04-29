# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-460kT'
    dbObj.maxRange_m=25170.238281
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=506000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=230000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
