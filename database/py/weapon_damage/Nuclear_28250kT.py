import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-28250kT'
    dbObj.maxRange_m=86569.625000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=31075000320.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=14124999680.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
