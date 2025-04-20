import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-380kT'
    dbObj.maxRange_m=23768.132812
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=418000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=190000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
