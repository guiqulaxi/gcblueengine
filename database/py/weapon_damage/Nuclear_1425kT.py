import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-1425kT'
    dbObj.maxRange_m=35334.949219
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=1567500032.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=712499968.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
