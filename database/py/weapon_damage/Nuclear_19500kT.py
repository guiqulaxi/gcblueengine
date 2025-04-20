import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-19500kT'
    dbObj.maxRange_m=77458.734375
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=21450000384.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=9749999616.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
