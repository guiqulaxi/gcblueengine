# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis950kg'
    dbObj.maxRange_m=6599.124023
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=124.353897
    dbObj.fragCharge_kg=468.097412
    dbObj.radCharge_kg=12.435390
    dbObj.fragMetal_kg=357.548706
    dbObj.fragFragment_kg=0.127061
    dbObj.fragSpread=0.300000
    return dbObj
