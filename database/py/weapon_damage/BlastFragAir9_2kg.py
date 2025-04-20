import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir9.2kg'
    dbObj.maxRange_m=2264.013428
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.256463
    dbObj.fragCharge_kg=3.831692
    dbObj.radCharge_kg=0.225646
    dbObj.fragMetal_kg=3.111846
    dbObj.fragFragment_kg=0.013954
    dbObj.fragSpread=0.095928
    return dbObj
