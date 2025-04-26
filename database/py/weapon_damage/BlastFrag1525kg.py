# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1525kg'
    dbObj.maxRange_m=5413.783691
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=548.819214
    dbObj.fragCharge_kg=472.870514
    dbObj.radCharge_kg=54.881924
    dbObj.fragMetal_kg=503.310272
    dbObj.fragFragment_kg=0.088115
    dbObj.fragSpread=0.300000
    return dbObj
