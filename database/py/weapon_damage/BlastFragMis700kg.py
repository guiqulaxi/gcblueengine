# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis700kg'
    dbObj.maxRange_m=6031.254883
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=96.901337
    dbObj.fragCharge_kg=341.399109
    dbObj.radCharge_kg=9.690133
    dbObj.fragMetal_kg=261.699554
    dbObj.fragFragment_kg=0.104596
    dbObj.fragSpread=0.300000
    return dbObj
