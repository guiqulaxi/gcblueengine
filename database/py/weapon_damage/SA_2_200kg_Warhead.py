import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='SA-2 200kg Warhead'
    dbObj.maxRange_m=300.848236
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=70.000000
    dbObj.fragCharge_kg=70.000000
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=130.000000
    dbObj.fragFragment_kg=0.150000
    dbObj.fragSpread=0.800000
    return dbObj
