import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis680kg'
    dbObj.maxRange_m=5976.672363
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=94.618874
    dbObj.fragCharge_kg=331.320740
    dbObj.radCharge_kg=9.461887
    dbObj.fragMetal_kg=254.060379
    dbObj.fragFragment_kg=0.102568
    dbObj.fragSpread=0.300000
    return dbObj
