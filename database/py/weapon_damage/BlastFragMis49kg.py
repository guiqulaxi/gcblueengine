# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis49kg'
    dbObj.maxRange_m=3420.930420
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.996779
    dbObj.fragCharge_kg=21.755480
    dbObj.radCharge_kg=0.999678
    dbObj.fragMetal_kg=17.247740
    dbObj.fragFragment_kg=0.031822
    dbObj.fragSpread=0.300000
    return dbObj
