import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-4200kT'
    dbObj.maxRange_m=48869.148438
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=4620000256.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2100000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
