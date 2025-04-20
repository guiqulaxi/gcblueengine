import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-230kT'
    dbObj.maxRange_m=20444.587891
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=253000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=115000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
