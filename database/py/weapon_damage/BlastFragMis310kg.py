# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis310kg'
    dbObj.maxRange_m=4792.733887
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=49.140804
    dbObj.fragCharge_kg=147.039459
    dbObj.radCharge_kg=4.914080
    dbObj.fragMetal_kg=113.819733
    dbObj.fragFragment_kg=0.064052
    dbObj.fragSpread=0.300000
    return dbObj
