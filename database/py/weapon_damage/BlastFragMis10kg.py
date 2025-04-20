import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis10kg'
    dbObj.maxRange_m=2327.992920
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.432113
    dbObj.fragCharge_kg=4.178592
    dbObj.radCharge_kg=0.243211
    dbObj.fragMetal_kg=3.389296
    dbObj.fragFragment_kg=0.014736
    dbObj.fragSpread=0.102045
    return dbObj
