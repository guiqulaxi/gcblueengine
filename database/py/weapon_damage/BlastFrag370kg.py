# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag370kg'
    dbObj.maxRange_m=3003.241455
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=133.054153
    dbObj.fragCharge_kg=114.797234
    dbObj.radCharge_kg=13.305415
    dbObj.fragMetal_kg=122.148613
    dbObj.fragFragment_kg=0.025967
    dbObj.fragSpread=0.300000
    return dbObj
