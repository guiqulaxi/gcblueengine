import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-10000kT'
    dbObj.maxRange_m=63395.726562
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=11000000512.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=5000000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
