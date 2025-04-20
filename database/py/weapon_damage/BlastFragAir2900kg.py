import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2900kg'
    dbObj.maxRange_m=10220.055664
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=299.786896
    dbObj.fragCharge_kg=1482.142090
    dbObj.radCharge_kg=29.978691
    dbObj.fragMetal_kg=1118.071045
    dbObj.fragFragment_kg=0.333553
    dbObj.fragSpread=0.300000
    return dbObj
