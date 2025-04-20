import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast200kg'
    dbObj.maxRange_m=73.038879
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=200.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=20.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
