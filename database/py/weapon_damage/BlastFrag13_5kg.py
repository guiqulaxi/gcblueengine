# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag13.5kg'
    dbObj.maxRange_m=665.055176
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.795810
    dbObj.fragCharge_kg=4.227794
    dbObj.radCharge_kg=0.479581
    dbObj.fragMetal_kg=4.476397
    dbObj.fragFragment_kg=0.001675
    dbObj.fragSpread=0.300000
    return dbObj
