# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis115kg'
    dbObj.maxRange_m=3977.048584
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=21.042191
    dbObj.fragCharge_kg=52.671871
    dbObj.radCharge_kg=2.104219
    dbObj.fragMetal_kg=41.285934
    dbObj.fragFragment_kg=0.043368
    dbObj.fragSpread=0.300000
    return dbObj
