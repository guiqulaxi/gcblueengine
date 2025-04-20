import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast48kg'
    dbObj.maxRange_m=45.411350
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=48.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=4.800000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
