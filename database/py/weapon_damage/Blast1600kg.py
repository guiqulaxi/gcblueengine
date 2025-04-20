import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1600kg'
    dbObj.maxRange_m=145.976532
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1600.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=160.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
