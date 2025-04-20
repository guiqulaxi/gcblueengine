import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-21250kT'
    dbObj.maxRange_m=79481.796875
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=23374999552.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=10625000448.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
