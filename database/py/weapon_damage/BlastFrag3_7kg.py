# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.7kg'
    dbObj.maxRange_m=341.590881
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.299733
    dbObj.fragCharge_kg=1.168512
    dbObj.radCharge_kg=0.129973
    dbObj.fragMetal_kg=1.231756
    dbObj.fragFragment_kg=0.000631
    dbObj.fragSpread=0.300000
    return dbObj
