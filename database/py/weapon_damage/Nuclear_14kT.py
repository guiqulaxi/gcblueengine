import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-14kT'
    dbObj.maxRange_m=8828.733398
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=15400000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=7000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
