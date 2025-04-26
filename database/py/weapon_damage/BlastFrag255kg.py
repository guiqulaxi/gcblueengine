# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag255kg'
    dbObj.maxRange_m=2596.478516
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=91.663338
    dbObj.fragCharge_kg=79.141113
    dbObj.radCharge_kg=9.166333
    dbObj.fragMetal_kg=84.195557
    dbObj.fragFragment_kg=0.019418
    dbObj.fragSpread=0.300000
    return dbObj
