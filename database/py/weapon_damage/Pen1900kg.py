import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1900kg'
    dbObj.maxRange_m=137.263062
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1330.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=190.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
