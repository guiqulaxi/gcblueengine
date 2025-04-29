# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1400kg'
    dbObj.maxRange_m=139.627747
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1400.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=140.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
