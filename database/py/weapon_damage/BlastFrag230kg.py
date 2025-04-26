# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag230kg'
    dbObj.maxRange_m=2487.749512
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=82.665878
    dbObj.fragCharge_kg=71.389412
    dbObj.radCharge_kg=8.266588
    dbObj.fragMetal_kg=75.944710
    dbObj.fragFragment_kg=0.017844
    dbObj.fragSpread=0.300000
    return dbObj
