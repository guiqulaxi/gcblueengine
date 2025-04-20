import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-140kT'
    dbObj.maxRange_m=17615.638672
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=154000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=70000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
