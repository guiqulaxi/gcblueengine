# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag14.5kg'
    dbObj.maxRange_m=690.250244
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.154047
    dbObj.fragCharge_kg=4.538969
    dbObj.radCharge_kg=0.515405
    dbObj.fragMetal_kg=4.806984
    dbObj.fragFragment_kg=0.001778
    dbObj.fragSpread=0.300000
    return dbObj
