import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir540kg'
    dbObj.maxRange_m=5541.410156
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=78.208641
    dbObj.fragCharge_kg=261.060913
    dbObj.radCharge_kg=7.820864
    dbObj.fragMetal_kg=200.730453
    dbObj.fragFragment_kg=0.087198
    dbObj.fragSpread=0.300000
    return dbObj
