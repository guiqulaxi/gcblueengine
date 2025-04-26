# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir11.5kg'
    dbObj.maxRange_m=2439.957275
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.757290
    dbObj.fragCharge_kg=4.831807
    dbObj.radCharge_kg=0.275729
    dbObj.fragMetal_kg=3.910903
    dbObj.fragFragment_kg=0.016161
    dbObj.fragSpread=0.112971
    return dbObj
