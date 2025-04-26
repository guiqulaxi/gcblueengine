# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.6kg'
    dbObj.maxRange_m=141.373154
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.216000
    dbObj.fragCharge_kg=0.186000
    dbObj.radCharge_kg=0.021600
    dbObj.fragMetal_kg=0.198000
    dbObj.fragFragment_kg=0.000231
    dbObj.fragSpread=0.300000
    return dbObj
