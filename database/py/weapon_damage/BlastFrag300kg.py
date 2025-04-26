# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag300kg'
    dbObj.maxRange_m=2771.635498
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=107.859329
    dbObj.fragCharge_kg=93.093781
    dbObj.radCharge_kg=10.785933
    dbObj.fragMetal_kg=99.046890
    dbObj.fragFragment_kg=0.022109
    dbObj.fragSpread=0.300000
    return dbObj
