import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1900kg'
    dbObj.maxRange_m=5885.789062
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=683.813782
    dbObj.fragCharge_kg=589.124146
    dbObj.radCharge_kg=68.381378
    dbObj.fragMetal_kg=627.062073
    dbObj.fragFragment_kg=0.105353
    dbObj.fragSpread=0.300000
    return dbObj
