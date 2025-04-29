# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag325kg'
    dbObj.maxRange_m=2859.399414
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=116.857353
    dbObj.fragCharge_kg=100.845100
    dbObj.radCharge_kg=11.685736
    dbObj.fragMetal_kg=107.297546
    dbObj.fragFragment_kg=0.023530
    dbObj.fragSpread=0.300000
    return dbObj
