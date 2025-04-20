import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-260kT'
    dbObj.maxRange_m=21210.552734
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=286000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=130000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
