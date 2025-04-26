# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1575kg'
    dbObj.maxRange_m=5481.960938
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=566.818420
    dbObj.fragCharge_kg=488.371033
    dbObj.radCharge_kg=56.681843
    dbObj.fragMetal_kg=519.810547
    dbObj.fragFragment_kg=0.090496
    dbObj.fragSpread=0.300000
    return dbObj
