# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag42kg'
    dbObj.maxRange_m=1132.778809
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=15.027818
    dbObj.fragCharge_kg=13.081455
    dbObj.radCharge_kg=1.502782
    dbObj.fragMetal_kg=13.890727
    dbObj.fragFragment_kg=0.004095
    dbObj.fragSpread=0.300000
    return dbObj
