# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag10kg'
    dbObj.maxRange_m=564.285034
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.543211
    dbObj.fragCharge_kg=3.137859
    dbObj.radCharge_kg=0.354321
    dbObj.fragMetal_kg=3.318930
    dbObj.fragFragment_kg=0.001296
    dbObj.fragSpread=0.300000
    return dbObj
