import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Mk-13 Mod4 GMLS'
    dbObj.natoClass=''
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=0.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=0.000000
    dbObj.height_m=0.000000
    dbObj.childClassList=['RGM-84A Harpoon','RGM-84C Harpoon','RGM-84D Harpoon','RGM-84F Harpoon','RGM-84G Harpoon','RIM-66A','RIM-66B','RIM-66E','RIM-66G','RIM-66L']
    dbObj.childCapacityList=[1,1,1,1,1,1,1,1,1,1]
    dbObj.childLoadTime_s=[6.640000,6.640000,6.640000,6.640000,6.640000,6.640000,6.640000,6.640000,6.640000,6.640000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
