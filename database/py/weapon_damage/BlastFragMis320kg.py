import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis320kg'
    dbObj.maxRange_m=4834.851074
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=50.475426
    dbObj.fragCharge_kg=151.949722
    dbObj.radCharge_kg=5.047543
    dbObj.fragMetal_kg=117.574860
    dbObj.fragFragment_kg=0.065247
    dbObj.fragSpread=0.300000
    return dbObj
