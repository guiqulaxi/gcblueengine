import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-43500kT'
    dbObj.maxRange_m=98538.687500
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=47850000384.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=21749999616.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
