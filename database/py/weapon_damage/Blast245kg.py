import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast245kg'
    dbObj.maxRange_m=78.145401
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=245.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=24.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
