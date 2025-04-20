import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-12500kT'
    dbObj.maxRange_m=67784.906250
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=13749999616.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=6249999872.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
