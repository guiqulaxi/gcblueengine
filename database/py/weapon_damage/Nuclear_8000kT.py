import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-8000kT'
    dbObj.maxRange_m=59290.757812
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=8800000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=4000000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
