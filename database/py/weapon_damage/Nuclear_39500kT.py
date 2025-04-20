import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-39500kT'
    dbObj.maxRange_m=95728.031250
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=43449999360.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=19750000640.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
