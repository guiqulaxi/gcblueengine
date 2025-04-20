import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-1325kT'
    dbObj.maxRange_m=34572.019531
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=1457500032.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=662499968.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
