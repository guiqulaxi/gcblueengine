import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast24.5kg'
    dbObj.maxRange_m=36.299728
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=24.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.450000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
