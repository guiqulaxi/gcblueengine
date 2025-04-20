import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-36000kT'
    dbObj.maxRange_m=93100.226562
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=39600001024.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=17999998976.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
