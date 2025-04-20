import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2900kg'
    dbObj.maxRange_m=177.946564
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2900.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=290.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
