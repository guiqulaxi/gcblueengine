# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1800kg'
    dbObj.maxRange_m=5768.195801
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=647.815125
    dbObj.fragCharge_kg=558.123230
    dbObj.radCharge_kg=64.781517
    dbObj.fragMetal_kg=594.061646
    dbObj.fragFragment_kg=0.100894
    dbObj.fragSpread=0.300000
    return dbObj
