import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-34750kT'
    dbObj.maxRange_m=92118.414062
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=38224998400.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=17375000576.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
