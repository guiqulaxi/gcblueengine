import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir315kg'
    dbObj.maxRange_m=4814.622559
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=49.809093
    dbObj.fragCharge_kg=149.493942
    dbObj.radCharge_kg=4.980909
    dbObj.fragMetal_kg=115.696968
    dbObj.fragFragment_kg=0.064671
    dbObj.fragSpread=0.300000
    return dbObj
