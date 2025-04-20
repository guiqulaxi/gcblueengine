import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast4.7kg'
    dbObj.maxRange_m=20.946899
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.700000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.470000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
