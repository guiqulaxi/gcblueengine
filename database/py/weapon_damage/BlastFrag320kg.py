import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag320kg'
    dbObj.maxRange_m=2842.332031
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=115.057739
    dbObj.fragCharge_kg=99.294846
    dbObj.radCharge_kg=11.505774
    dbObj.fragMetal_kg=105.647423
    dbObj.fragFragment_kg=0.023250
    dbObj.fragSpread=0.300000
    return dbObj
