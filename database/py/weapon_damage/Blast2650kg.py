import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2650kg'
    dbObj.maxRange_m=172.683945
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2650.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=265.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
