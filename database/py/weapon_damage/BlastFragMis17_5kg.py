import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis17.5kg'
    dbObj.maxRange_m=2766.286621
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.014665
    dbObj.fragCharge_kg=7.473557
    dbObj.radCharge_kg=0.401467
    dbObj.fragMetal_kg=6.011778
    dbObj.fragFragment_kg=0.020730
    dbObj.fragSpread=0.162230
    return dbObj
