import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='DART 0.4kg'
    dbObj.maxRange_m=63.621658
    dbObj.probDetonate=1.000000
    dbObj.blastCharge_kg=0.020000
    dbObj.fragCharge_kg=0.200000
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=0.400000
    dbObj.fragFragment_kg=0.010000
    dbObj.fragSpread=0.250000
    return dbObj
