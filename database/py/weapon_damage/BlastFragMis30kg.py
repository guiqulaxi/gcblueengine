# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis30kg'
    dbObj.maxRange_m=3141.338135
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.483485
    dbObj.fragCharge_kg=13.077677
    dbObj.radCharge_kg=0.648348
    dbObj.fragMetal_kg=10.438839
    dbObj.fragFragment_kg=0.026766
    dbObj.fragSpread=0.293403
    return dbObj
