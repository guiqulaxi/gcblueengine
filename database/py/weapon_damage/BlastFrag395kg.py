# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag395kg'
    dbObj.maxRange_m=3076.373291
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=142.052536
    dbObj.fragCharge_kg=122.548302
    dbObj.radCharge_kg=14.205255
    dbObj.fragMetal_kg=130.399155
    dbObj.fragFragment_kg=0.027257
    dbObj.fragSpread=0.300000
    return dbObj
