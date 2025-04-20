import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-5800kT'
    dbObj.maxRange_m=53837.933594
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=6380000256.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2900000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
