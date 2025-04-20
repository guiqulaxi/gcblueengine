import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3400kg'
    dbObj.maxRange_m=7413.005371
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1223.799438
    dbObj.fragCharge_kg=1054.133667
    dbObj.radCharge_kg=122.379944
    dbObj.fragMetal_kg=1122.066895
    dbObj.fragFragment_kg=0.173587
    dbObj.fragSpread=0.300000
    return dbObj
