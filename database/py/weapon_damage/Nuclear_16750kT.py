import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-16750kT'
    dbObj.maxRange_m=74005.578125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=18424999936.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=8375000064.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
