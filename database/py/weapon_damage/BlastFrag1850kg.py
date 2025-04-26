# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1850kg'
    dbObj.maxRange_m=5827.673828
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=665.814453
    dbObj.fragCharge_kg=573.623718
    dbObj.radCharge_kg=66.581444
    dbObj.fragMetal_kg=610.561829
    dbObj.fragFragment_kg=0.103135
    dbObj.fragSpread=0.300000
    return dbObj
