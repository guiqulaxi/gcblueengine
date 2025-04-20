import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-18250kT'
    dbObj.maxRange_m=75934.453125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=20074999808.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=9125000192.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
