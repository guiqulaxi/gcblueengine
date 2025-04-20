import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag40kg'
    dbObj.maxRange_m=1107.795410
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=14.309021
    dbObj.fragCharge_kg=12.460652
    dbObj.radCharge_kg=1.430902
    dbObj.fragMetal_kg=13.230327
    dbObj.fragFragment_kg=0.003938
    dbObj.fragSpread=0.300000
    return dbObj
