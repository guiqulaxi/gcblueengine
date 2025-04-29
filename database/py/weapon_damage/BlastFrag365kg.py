# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag365kg'
    dbObj.maxRange_m=2988.068115
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=131.254486
    dbObj.fragCharge_kg=113.247009
    dbObj.radCharge_kg=13.125449
    dbObj.fragMetal_kg=120.498505
    dbObj.fragFragment_kg=0.025704
    dbObj.fragSpread=0.300000
    return dbObj
