# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag29kg'
    dbObj.maxRange_m=952.243774
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=10.356953
    dbObj.fragCharge_kg=9.045365
    dbObj.radCharge_kg=1.035695
    dbObj.fragMetal_kg=9.597683
    dbObj.fragFragment_kg=0.003030
    dbObj.fragSpread=0.300000
    return dbObj
