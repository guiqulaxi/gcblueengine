import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-125kT'
    dbObj.maxRange_m=17026.798828
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=137500000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=62500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
