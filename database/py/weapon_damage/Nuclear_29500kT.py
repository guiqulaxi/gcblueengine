import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-29500kT'
    dbObj.maxRange_m=87701.414062
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=32450000896.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=14750000128.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
