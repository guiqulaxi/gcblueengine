import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir740kg'
    dbObj.maxRange_m=6135.652832
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=101.424370
    dbObj.fragCharge_kg=361.583740
    dbObj.radCharge_kg=10.142437
    dbObj.fragMetal_kg=276.991882
    dbObj.fragFragment_kg=0.108539
    dbObj.fragSpread=0.300000
    return dbObj
