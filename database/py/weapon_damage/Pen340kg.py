import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen340kg'
    dbObj.maxRange_m=77.394699
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=238.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=34.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
