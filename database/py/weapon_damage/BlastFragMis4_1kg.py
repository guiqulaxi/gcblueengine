import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis4.1kg'
    dbObj.maxRange_m=1633.147705
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.087323
    dbObj.fragCharge_kg=1.653118
    dbObj.radCharge_kg=0.108732
    dbObj.fragMetal_kg=1.359559
    dbObj.fragFragment_kg=0.007470
    dbObj.fragSpread=0.063897
    return dbObj
