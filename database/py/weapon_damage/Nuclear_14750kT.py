import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-14750kT'
    dbObj.maxRange_m=71235.687500
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=16225000448.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=7375000064.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
