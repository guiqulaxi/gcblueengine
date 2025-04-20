import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir4.3kg'
    dbObj.maxRange_m=1666.495239
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.135312
    dbObj.fragCharge_kg=1.737125
    dbObj.radCharge_kg=0.113531
    dbObj.fragMetal_kg=1.427563
    dbObj.fragFragment_kg=0.007758
    dbObj.fragSpread=0.065309
    return dbObj
