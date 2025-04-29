# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3900kg'
    dbObj.maxRange_m=7805.000977
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1403.796021
    dbObj.fragCharge_kg=1209.135986
    dbObj.radCharge_kg=140.379608
    dbObj.fragMetal_kg=1287.067993
    dbObj.fragFragment_kg=0.194304
    dbObj.fragSpread=0.300000
    return dbObj
