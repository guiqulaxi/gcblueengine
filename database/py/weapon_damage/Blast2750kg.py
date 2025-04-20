import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2750kg'
    dbObj.maxRange_m=174.827148
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2750.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=275.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
