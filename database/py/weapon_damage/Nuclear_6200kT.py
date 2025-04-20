import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-6200kT'
    dbObj.maxRange_m=54925.941406
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=6819999744.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=3100000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
