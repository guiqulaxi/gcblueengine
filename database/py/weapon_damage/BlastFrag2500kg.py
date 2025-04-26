# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2500kg'
    dbObj.maxRange_m=6571.656738
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=899.807007
    dbObj.fragCharge_kg=775.128662
    dbObj.radCharge_kg=89.980705
    dbObj.fragMetal_kg=825.064331
    dbObj.fragFragment_kg=0.133592
    dbObj.fragSpread=0.300000
    return dbObj
