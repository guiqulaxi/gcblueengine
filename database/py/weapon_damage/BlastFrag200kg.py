import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag200kg'
    dbObj.maxRange_m=2344.006348
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=71.869324
    dbObj.fragCharge_kg=62.087116
    dbObj.radCharge_kg=7.186933
    dbObj.fragMetal_kg=66.043556
    dbObj.fragFragment_kg=0.015876
    dbObj.fragSpread=0.300000
    return dbObj
