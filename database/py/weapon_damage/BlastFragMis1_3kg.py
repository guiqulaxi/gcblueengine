# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1.3kg'
    dbObj.maxRange_m=908.783813
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.381588
    dbObj.fragCharge_kg=0.499608
    dbObj.radCharge_kg=0.038159
    dbObj.fragMetal_kg=0.418804
    dbObj.fragFragment_kg=0.002618
    dbObj.fragSpread=0.049383
    return dbObj
