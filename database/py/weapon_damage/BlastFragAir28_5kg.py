# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir28.5kg'
    dbObj.maxRange_m=3108.478516
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.195364
    dbObj.fragCharge_kg=12.399757
    dbObj.radCharge_kg=0.619536
    dbObj.fragMetal_kg=9.904879
    dbObj.fragFragment_kg=0.026203
    dbObj.fragSpread=0.275625
    return dbObj
