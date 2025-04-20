import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast31kg'
    dbObj.maxRange_m=39.258579
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=31.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=3.100000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
