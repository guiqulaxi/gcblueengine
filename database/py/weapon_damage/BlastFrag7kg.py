import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag7kg'
    dbObj.maxRange_m=475.358246
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.472008
    dbObj.fragCharge_kg=2.201995
    dbObj.radCharge_kg=0.247201
    dbObj.fragMetal_kg=2.325997
    dbObj.fragFragment_kg=0.001003
    dbObj.fragSpread=0.300000
    return dbObj
