import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag460kg'
    dbObj.maxRange_m=3289.551514
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=165.448792
    dbObj.fragCharge_kg=142.700806
    dbObj.radCharge_kg=16.544878
    dbObj.fragMetal_kg=151.850403
    dbObj.fragFragment_kg=0.031219
    dbObj.fragSpread=0.300000
    return dbObj
