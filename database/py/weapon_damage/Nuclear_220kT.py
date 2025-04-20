import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-220kT'
    dbObj.maxRange_m=20173.757812
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=242000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=110000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
