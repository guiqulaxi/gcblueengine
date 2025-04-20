import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-1050kT'
    dbObj.maxRange_m=32241.615234
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=1155000064.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=525000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
