import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag130kg'
    dbObj.maxRange_m=1930.548462
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=46.679951
    dbObj.fragCharge_kg=40.380032
    dbObj.radCharge_kg=4.667995
    dbObj.fragMetal_kg=42.940018
    dbObj.fragFragment_kg=0.010910
    dbObj.fragSpread=0.300000
    return dbObj
