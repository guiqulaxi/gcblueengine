# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3800kg'
    dbObj.maxRange_m=7730.097168
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1367.796753
    dbObj.fragCharge_kg=1178.135498
    dbObj.radCharge_kg=136.779678
    dbObj.fragMetal_kg=1254.067749
    dbObj.fragFragment_kg=0.190241
    dbObj.fragSpread=0.300000
    return dbObj
