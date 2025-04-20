import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast39kg'
    dbObj.maxRange_m=42.377529
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=39.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=3.900000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
