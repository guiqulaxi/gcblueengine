import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-10250kT'
    dbObj.maxRange_m=63867.093750
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=11274999808.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=5125000192.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
