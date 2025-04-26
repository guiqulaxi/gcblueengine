# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1.4kg'
    dbObj.maxRange_m=946.691040
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.408382
    dbObj.fragCharge_kg=0.539745
    dbObj.radCharge_kg=0.040838
    dbObj.fragMetal_kg=0.451873
    dbObj.fragFragment_kg=0.002807
    dbObj.fragSpread=0.050002
    return dbObj
