# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis4kg'
    dbObj.maxRange_m=1611.213013
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.063239
    dbObj.fragCharge_kg=1.611174
    dbObj.radCharge_kg=0.106324
    dbObj.fragMetal_kg=1.325587
    dbObj.fragFragment_kg=0.007283
    dbObj.fragSpread=0.063897
    return dbObj
