# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis9kg'
    dbObj.maxRange_m=2243.222900
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.212288
    dbObj.fragCharge_kg=3.745141
    dbObj.radCharge_kg=0.221229
    dbObj.fragMetal_kg=3.042571
    dbObj.fragFragment_kg=0.013705
    dbObj.fragSpread=0.095069
    return dbObj
