import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-30000kT'
    dbObj.maxRange_m=88144.734375
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=32999999488.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=15000000512.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
