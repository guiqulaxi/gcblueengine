# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis6.6kg'
    dbObj.maxRange_m=1998.940918
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.672830
    dbObj.fragCharge_kg=2.712780
    dbObj.radCharge_kg=0.167283
    dbObj.fragMetal_kg=2.214390
    dbObj.fragFragment_kg=0.010962
    dbObj.fragSpread=0.078711
    return dbObj
