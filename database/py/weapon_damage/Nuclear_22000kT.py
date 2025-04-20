import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-22000kT'
    dbObj.maxRange_m=80313.171875
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=24199999488.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=11000000512.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
