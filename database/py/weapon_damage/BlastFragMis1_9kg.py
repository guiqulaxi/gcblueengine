# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1.9kg'
    dbObj.maxRange_m=1117.517944
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.539923
    dbObj.fragCharge_kg=0.742051
    dbObj.radCharge_kg=0.053992
    dbObj.fragMetal_kg=0.618026
    dbObj.fragFragment_kg=0.003746
    dbObj.fragSpread=0.052517
    return dbObj
