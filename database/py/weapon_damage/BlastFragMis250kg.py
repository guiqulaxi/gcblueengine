import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis250kg'
    dbObj.maxRange_m=4502.199707
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=40.956005
    dbObj.fragCharge_kg=117.695999
    dbObj.radCharge_kg=4.095601
    dbObj.fragMetal_kg=91.348000
    dbObj.fragFragment_kg=0.056145
    dbObj.fragSpread=0.300000
    return dbObj
