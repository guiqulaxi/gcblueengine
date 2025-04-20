import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-4600kT'
    dbObj.maxRange_m=50221.230469
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=5059999744.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2300000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
