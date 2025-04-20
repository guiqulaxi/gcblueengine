import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis9.4kg'
    dbObj.maxRange_m=2279.255615
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.300531
    dbObj.fragCharge_kg=3.918313
    dbObj.radCharge_kg=0.230053
    dbObj.fragMetal_kg=3.181156
    dbObj.fragFragment_kg=0.014138
    dbObj.fragSpread=0.097656
    return dbObj
