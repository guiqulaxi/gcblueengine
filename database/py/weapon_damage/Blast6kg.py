import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast6kg'
    dbObj.maxRange_m=22.721420
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.600000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
