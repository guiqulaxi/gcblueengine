# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir8.2kg'
    dbObj.maxRange_m=2171.427979
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.034467
    dbObj.fragCharge_kg=3.399689
    dbObj.radCharge_kg=0.203447
    dbObj.fragMetal_kg=2.765845
    dbObj.fragFragment_kg=0.012864
    dbObj.fragSpread=0.089169
    return dbObj
