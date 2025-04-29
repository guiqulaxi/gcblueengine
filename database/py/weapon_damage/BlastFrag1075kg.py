# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1075kg'
    dbObj.maxRange_m=4703.215820
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=386.827850
    dbObj.fragCharge_kg=333.364777
    dbObj.radCharge_kg=38.682785
    dbObj.fragMetal_kg=354.807373
    dbObj.fragFragment_kg=0.065414
    dbObj.fragSpread=0.300000
    return dbObj
