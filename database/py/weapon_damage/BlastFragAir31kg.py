import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir31kg'
    dbObj.maxRange_m=3161.997559
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.674531
    dbObj.fragCharge_kg=13.530313
    dbObj.radCharge_kg=0.667453
    dbObj.fragMetal_kg=10.795156
    dbObj.fragFragment_kg=0.027124
    dbObj.fragSpread=0.300000
    return dbObj
