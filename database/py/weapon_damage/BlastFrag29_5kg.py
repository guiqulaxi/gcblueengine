# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag29.5kg'
    dbObj.maxRange_m=958.960571
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=10.536530
    dbObj.fragCharge_kg=9.200646
    dbObj.radCharge_kg=1.053653
    dbObj.fragMetal_kg=9.762823
    dbObj.fragFragment_kg=0.003066
    dbObj.fragSpread=0.300000
    return dbObj
