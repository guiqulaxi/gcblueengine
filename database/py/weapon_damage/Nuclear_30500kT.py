import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-30500kT'
    dbObj.maxRange_m=88582.906250
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=33550000128.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=15249999872.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
