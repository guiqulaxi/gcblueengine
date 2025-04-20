import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-4800kT'
    dbObj.maxRange_m=50866.558594
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=5280000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2400000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
