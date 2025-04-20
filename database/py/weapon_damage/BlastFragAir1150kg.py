import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1150kg'
    dbObj.maxRange_m=7103.253418
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=145.114868
    dbObj.fragCharge_kg=570.256775
    dbObj.radCharge_kg=14.511486
    dbObj.fragMetal_kg=434.628387
    dbObj.fragFragment_kg=0.149152
    dbObj.fragSpread=0.300000
    return dbObj
