import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1500kg'
    dbObj.maxRange_m=7931.021973
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=179.450684
    dbObj.fragCharge_kg=750.366211
    dbObj.radCharge_kg=17.945068
    dbObj.fragMetal_kg=570.183105
    dbObj.fragFragment_kg=0.189934
    dbObj.fragSpread=0.300000
    return dbObj
