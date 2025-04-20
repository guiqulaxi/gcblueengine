import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir67.5kg'
    dbObj.maxRange_m=3679.077393
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=13.237841
    dbObj.fragCharge_kg=30.324774
    dbObj.radCharge_kg=1.323784
    dbObj.fragMetal_kg=23.937387
    dbObj.fragFragment_kg=0.036940
    dbObj.fragSpread=0.300000
    return dbObj
