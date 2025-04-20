import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-24500kT'
    dbObj.maxRange_m=82948.742188
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=26950000640.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=12250000384.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
