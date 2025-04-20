import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2150kg'
    dbObj.maxRange_m=6180.377930
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=773.810730
    dbObj.fragCharge_kg=666.626160
    dbObj.radCharge_kg=77.381073
    dbObj.fragMetal_kg=709.563110
    dbObj.fragFragment_kg=0.117012
    dbObj.fragSpread=0.300000
    return dbObj
