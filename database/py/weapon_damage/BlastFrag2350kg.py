import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2350kg'
    dbObj.maxRange_m=6409.326660
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=845.808533
    dbObj.fragCharge_kg=728.627625
    dbObj.radCharge_kg=84.580856
    dbObj.fragMetal_kg=775.563843
    dbObj.fragFragment_kg=0.126561
    dbObj.fragSpread=0.300000
    return dbObj
