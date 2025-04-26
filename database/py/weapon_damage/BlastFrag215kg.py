# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag215kg'
    dbObj.maxRange_m=2417.855469
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=77.267540
    dbObj.fragCharge_kg=66.738304
    dbObj.radCharge_kg=7.726754
    dbObj.fragMetal_kg=70.994156
    dbObj.fragFragment_kg=0.016871
    dbObj.fragSpread=0.300000
    return dbObj
