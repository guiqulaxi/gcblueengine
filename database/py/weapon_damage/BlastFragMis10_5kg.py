# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis10.5kg'
    dbObj.maxRange_m=2367.171143
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.541084
    dbObj.fragCharge_kg=4.395944
    dbObj.radCharge_kg=0.254108
    dbObj.fragMetal_kg=3.562972
    dbObj.fragFragment_kg=0.015226
    dbObj.fragSpread=0.105625
    return dbObj
