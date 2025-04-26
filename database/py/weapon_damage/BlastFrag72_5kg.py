# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag72.5kg'
    dbObj.maxRange_m=1469.109619
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=25.994354
    dbObj.fragCharge_kg=22.545431
    dbObj.radCharge_kg=2.599435
    dbObj.fragMetal_kg=23.960215
    dbObj.fragFragment_kg=0.006539
    dbObj.fragSpread=0.300000
    return dbObj
