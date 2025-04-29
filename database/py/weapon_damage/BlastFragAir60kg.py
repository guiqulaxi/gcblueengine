# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir60kg'
    dbObj.maxRange_m=3581.639648
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=11.941262
    dbObj.fragCharge_kg=26.839159
    dbObj.radCharge_kg=1.194126
    dbObj.fragMetal_kg=21.219580
    dbObj.fragFragment_kg=0.034958
    dbObj.fragSpread=0.300000
    return dbObj
