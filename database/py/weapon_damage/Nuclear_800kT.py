import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-800kT'
    dbObj.maxRange_m=29715.769531
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=880000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=400000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
