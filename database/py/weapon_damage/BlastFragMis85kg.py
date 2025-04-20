import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis85kg'
    dbObj.maxRange_m=3808.700439
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=16.186613
    dbObj.fragCharge_kg=38.508926
    dbObj.radCharge_kg=1.618661
    dbObj.fragMetal_kg=30.304462
    dbObj.fragFragment_kg=0.039666
    dbObj.fragSpread=0.300000
    return dbObj
