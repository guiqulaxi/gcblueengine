import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-15250kT'
    dbObj.maxRange_m=71951.679688
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=16775000064.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=7624999936.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
