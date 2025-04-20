import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1450kg'
    dbObj.maxRange_m=141.268921
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1450.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=145.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
