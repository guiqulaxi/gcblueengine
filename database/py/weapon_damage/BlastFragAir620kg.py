import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir620kg'
    dbObj.maxRange_m=5802.362793
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=87.682632
    dbObj.fragCharge_kg=301.144897
    dbObj.radCharge_kg=8.768264
    dbObj.fragMetal_kg=231.172455
    dbObj.fragFragment_kg=0.096242
    dbObj.fragSpread=0.300000
    return dbObj
