# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag680kg'
    dbObj.maxRange_m=3899.751221
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=244.639145
    dbObj.fragCharge_kg=210.907242
    dbObj.radCharge_kg=24.463915
    dbObj.fragMetal_kg=224.453613
    dbObj.fragFragment_kg=0.044253
    dbObj.fragSpread=0.300000
    return dbObj
