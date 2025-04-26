# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1225kg'
    dbObj.maxRange_m=4962.201660
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=440.824615
    dbObj.fragCharge_kg=379.866913
    dbObj.radCharge_kg=44.082462
    dbObj.fragMetal_kg=404.308472
    dbObj.fragFragment_kg=0.073244
    dbObj.fragSpread=0.300000
    return dbObj
