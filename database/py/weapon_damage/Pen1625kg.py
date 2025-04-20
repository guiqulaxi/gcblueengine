import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1625kg'
    dbObj.maxRange_m=130.299545
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1137.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=162.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
