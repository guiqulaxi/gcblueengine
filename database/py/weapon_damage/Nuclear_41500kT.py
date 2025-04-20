import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-41500kT'
    dbObj.maxRange_m=97157.070312
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=45650001920.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=20750000128.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
