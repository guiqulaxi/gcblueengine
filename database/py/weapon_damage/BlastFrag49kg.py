# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag49kg'
    dbObj.maxRange_m=1213.094482
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=17.544016
    dbObj.fragCharge_kg=15.253989
    dbObj.radCharge_kg=1.754402
    dbObj.fragMetal_kg=16.201994
    dbObj.fragFragment_kg=0.004624
    dbObj.fragSpread=0.300000
    return dbObj
