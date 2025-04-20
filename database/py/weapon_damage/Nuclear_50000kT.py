import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-50000kT'
    dbObj.maxRange_m=102742.703125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=54999998464.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=24999999488.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
