# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast3100kg'
    dbObj.maxRange_m=181.942657
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3100.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=310.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
