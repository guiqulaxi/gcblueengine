import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-30750kT'
    dbObj.maxRange_m=88800.117188
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=33824999424.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=15374999552.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
