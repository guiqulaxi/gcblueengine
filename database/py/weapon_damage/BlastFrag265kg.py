# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag265kg'
    dbObj.maxRange_m=2637.529053
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=95.262390
    dbObj.fragCharge_kg=82.241745
    dbObj.radCharge_kg=9.526238
    dbObj.fragMetal_kg=87.495872
    dbObj.fragFragment_kg=0.020031
    dbObj.fragSpread=0.300000
    return dbObj
