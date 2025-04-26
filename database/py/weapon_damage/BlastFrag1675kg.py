# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1675kg'
    dbObj.maxRange_m=5613.133789
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=602.816895
    dbObj.fragCharge_kg=519.372070
    dbObj.radCharge_kg=60.281693
    dbObj.fragMetal_kg=552.811035
    dbObj.fragFragment_kg=0.095181
    dbObj.fragSpread=0.300000
    return dbObj
