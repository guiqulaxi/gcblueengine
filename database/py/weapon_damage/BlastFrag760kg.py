# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag760kg'
    dbObj.maxRange_m=4083.773926
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=273.436401
    dbObj.fragCharge_kg=235.709061
    dbObj.radCharge_kg=27.343639
    dbObj.fragMetal_kg=250.854538
    dbObj.fragFragment_kg=0.048691
    dbObj.fragSpread=0.300000
    return dbObj
