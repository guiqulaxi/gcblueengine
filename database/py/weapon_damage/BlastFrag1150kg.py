# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1150kg'
    dbObj.maxRange_m=4835.921387
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=413.826172
    dbObj.fragCharge_kg=356.615875
    dbObj.radCharge_kg=41.382618
    dbObj.fragMetal_kg=379.557953
    dbObj.fragFragment_kg=0.069364
    dbObj.fragSpread=0.300000
    return dbObj
