import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir170kg'
    dbObj.maxRange_m=4266.525879
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=29.467056
    dbObj.fragCharge_kg=78.955299
    dbObj.radCharge_kg=2.946706
    dbObj.fragMetal_kg=61.577648
    dbObj.fragFragment_kg=0.050186
    dbObj.fragSpread=0.300000
    return dbObj
