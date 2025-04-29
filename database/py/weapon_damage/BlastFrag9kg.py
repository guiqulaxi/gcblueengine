# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag9kg'
    dbObj.maxRange_m=537.765991
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.185810
    dbObj.fragCharge_kg=2.826127
    dbObj.radCharge_kg=0.318581
    dbObj.fragMetal_kg=2.988063
    dbObj.fragFragment_kg=0.001205
    dbObj.fragSpread=0.300000
    return dbObj
