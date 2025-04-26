# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag11.5kg'
    dbObj.maxRange_m=610.162415
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.079764
    dbObj.fragCharge_kg=3.605157
    dbObj.radCharge_kg=0.407976
    dbObj.fragMetal_kg=3.815078
    dbObj.fragFragment_kg=0.001463
    dbObj.fragSpread=0.300000
    return dbObj
