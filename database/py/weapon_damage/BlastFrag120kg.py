# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag120kg'
    dbObj.maxRange_m=1859.101807
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=43.081924
    dbObj.fragCharge_kg=37.278717
    dbObj.radCharge_kg=4.308193
    dbObj.fragMetal_kg=39.639359
    dbObj.fragFragment_kg=0.010154
    dbObj.fragSpread=0.300000
    return dbObj
