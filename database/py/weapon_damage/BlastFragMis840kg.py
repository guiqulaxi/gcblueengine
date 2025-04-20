import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis840kg'
    dbObj.maxRange_m=6372.125000
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=112.504456
    dbObj.fragCharge_kg=412.197021
    dbObj.radCharge_kg=11.250445
    dbObj.fragMetal_kg=315.298523
    dbObj.fragFragment_kg=0.117781
    dbObj.fragSpread=0.300000
    return dbObj
