# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.3kg'
    dbObj.maxRange_m=321.305359
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.158554
    dbObj.fragCharge_kg=1.042631
    dbObj.radCharge_kg=0.115855
    dbObj.fragMetal_kg=1.098815
    dbObj.fragFragment_kg=0.000582
    dbObj.fragSpread=0.300000
    return dbObj
