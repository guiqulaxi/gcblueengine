import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2.8kg'
    dbObj.maxRange_m=1362.779663
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.768898
    dbObj.fragCharge_kg=1.111401
    dbObj.radCharge_kg=0.076890
    dbObj.fragMetal_kg=0.919701
    dbObj.fragFragment_kg=0.005347
    dbObj.fragSpread=0.057068
    return dbObj
