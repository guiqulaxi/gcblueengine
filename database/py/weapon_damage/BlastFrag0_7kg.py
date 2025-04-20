import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.7kg'
    dbObj.maxRange_m=148.610138
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.252000
    dbObj.fragCharge_kg=0.217000
    dbObj.radCharge_kg=0.025200
    dbObj.fragMetal_kg=0.231000
    dbObj.fragFragment_kg=0.000243
    dbObj.fragSpread=0.300000
    return dbObj
