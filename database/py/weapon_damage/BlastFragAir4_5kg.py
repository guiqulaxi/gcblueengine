# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir4.5kg'
    dbObj.maxRange_m=1698.528564
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.183072
    dbObj.fragCharge_kg=1.821285
    dbObj.radCharge_kg=0.118307
    dbObj.fragMetal_kg=1.495643
    dbObj.fragFragment_kg=0.008041
    dbObj.fragSpread=0.066736
    return dbObj
