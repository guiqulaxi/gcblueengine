import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir520kg'
    dbObj.maxRange_m=5470.235840
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=75.796036
    dbObj.fragCharge_kg=251.069305
    dbObj.radCharge_kg=7.579603
    dbObj.fragMetal_kg=193.134659
    dbObj.fragFragment_kg=0.084820
    dbObj.fragSpread=0.300000
    return dbObj
