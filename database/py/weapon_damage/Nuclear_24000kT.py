import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-24000kT'
    dbObj.maxRange_m=82437.226562
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=26400000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=12000000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
