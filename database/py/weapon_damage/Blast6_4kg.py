import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast6.4kg'
    dbObj.maxRange_m=23.215019
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.400000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.640000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
