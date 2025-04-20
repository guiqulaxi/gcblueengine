import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag70kg'
    dbObj.maxRange_m=1444.752686
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=25.095219
    dbObj.fragCharge_kg=21.769854
    dbObj.radCharge_kg=2.509522
    dbObj.fragMetal_kg=23.134928
    dbObj.fragFragment_kg=0.006342
    dbObj.fragSpread=0.300000
    return dbObj
