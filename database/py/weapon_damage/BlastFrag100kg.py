# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag100kg'
    dbObj.maxRange_m=1702.973633
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=35.886421
    dbObj.fragCharge_kg=31.075718
    dbObj.radCharge_kg=3.588642
    dbObj.fragMetal_kg=33.037861
    dbObj.fragFragment_kg=0.008604
    dbObj.fragSpread=0.300000
    return dbObj
