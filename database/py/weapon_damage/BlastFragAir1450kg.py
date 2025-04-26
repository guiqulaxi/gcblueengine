# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1450kg'
    dbObj.maxRange_m=7822.578125
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=174.681366
    dbObj.fragCharge_kg=724.545776
    dbObj.radCharge_kg=17.468136
    dbObj.fragMetal_kg=550.772888
    dbObj.fragFragment_kg=0.184267
    dbObj.fragSpread=0.300000
    return dbObj
