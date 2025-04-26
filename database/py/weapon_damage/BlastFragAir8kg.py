# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir8kg'
    dbObj.maxRange_m=2148.491943
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.989717
    dbObj.fragCharge_kg=3.313522
    dbObj.radCharge_kg=0.198972
    dbObj.fragMetal_kg=2.696761
    dbObj.fragFragment_kg=0.012602
    dbObj.fragSpread=0.088341
    return dbObj
