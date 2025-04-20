import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1875kg'
    dbObj.maxRange_m=5856.897949
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=674.814148
    dbObj.fragCharge_kg=581.373901
    dbObj.radCharge_kg=67.481415
    dbObj.fragMetal_kg=618.811951
    dbObj.fragFragment_kg=0.104247
    dbObj.fragSpread=0.300000
    return dbObj
