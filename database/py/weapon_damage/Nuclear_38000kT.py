import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-38000kT'
    dbObj.maxRange_m=94622.640625
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=41799999488.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=19000000512.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
