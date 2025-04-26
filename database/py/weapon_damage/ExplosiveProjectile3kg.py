# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='ExplosiveProjectile3kg'
    dbObj.maxRange_m=50.000000
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
