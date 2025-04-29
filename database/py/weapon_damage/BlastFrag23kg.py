# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag23kg'
    dbObj.maxRange_m=861.909302
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.202669
    dbObj.fragCharge_kg=7.181554
    dbObj.radCharge_kg=0.820267
    dbObj.fragMetal_kg=7.615777
    dbObj.fragFragment_kg=0.002559
    dbObj.fragSpread=0.300000
    return dbObj
