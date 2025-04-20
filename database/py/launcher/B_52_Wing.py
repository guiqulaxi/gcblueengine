import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='B-52 Wing'
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
    dbObj.childClassList=['AGM-84A Harpoon','AGM-84C Harpoon','AGM-84D Harpoon','AGM-84F Harpoon','GBU-32A(v)2','GBU-32C(v)4','M117','M118','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[4,4,4,4,6,6,12,6,12,12,9]
    dbObj.childLoadTime_s=[300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000]
    dbObj.childCycleTime_s=[0.500000,0.500000,0.500000,0.500000,0.030000,0.030000,0.030000,0.030000,0.030000,0.030000,0.030000]
    dbObj.CalculateParams()
    return dbObj
