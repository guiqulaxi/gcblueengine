import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis11kg'
    dbObj.maxRange_m=2404.443115
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.649467
    dbObj.fragCharge_kg=4.613689
    dbObj.radCharge_kg=0.264947
    dbObj.fragMetal_kg=3.736844
    dbObj.fragFragment_kg=0.015701
    dbObj.fragSpread=0.109267
    return dbObj
