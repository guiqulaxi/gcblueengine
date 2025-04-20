import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-87.5kT'
    dbObj.maxRange_m=15298.977539
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=96250000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=43750000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
