import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='25 mm MGS'
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
    dbObj.childClassList=['25mm APDS','25mm APDS-T','25mm FAPDS-T','25mm HEI','25mm HEI-T','25mm SAPHEI','25mm SAPHEI-T']
    dbObj.childCapacityList=[400,400,400,400,400,400,400]
    dbObj.childLoadTime_s=[17.000000,17.000000,17.000000,17.000000,17.000000,17.000000,17.000000]
    dbObj.childCycleTime_s=[0.300000,0.300000,0.300000,0.300000,0.300000,0.300000,0.300000]
    dbObj.CalculateParams()
    return dbObj
