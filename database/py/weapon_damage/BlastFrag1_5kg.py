# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.5kg'
    dbObj.maxRange_m=190.222458
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.530000
    dbObj.fragCharge_kg=0.471667
    dbObj.radCharge_kg=0.053000
    dbObj.fragMetal_kg=0.498333
    dbObj.fragFragment_kg=0.000311
    dbObj.fragSpread=0.300000
    return dbObj
