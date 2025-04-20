import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2.4kg'
    dbObj.maxRange_m=1261.137695
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.668180
    dbObj.fragCharge_kg=0.946547
    dbObj.radCharge_kg=0.066818
    dbObj.fragMetal_kg=0.785273
    dbObj.fragFragment_kg=0.004647
    dbObj.fragSpread=0.055095
    return dbObj
