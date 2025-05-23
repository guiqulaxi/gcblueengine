# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Hayabusa PGM durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.930000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=3.030000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.320000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=3.820000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=4.510000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=5.390000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=6.480000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=7.760000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=9.230000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=10.910000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=12.780000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=16.100000
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*24
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=75.029999
    dbObj.waterBlastEffect[1].damageFactor=0.048000
    dbObj.waterBlastEffect[2].effectLevel=85.152000
    dbObj.waterBlastEffect[2].damageFactor=0.050000
    dbObj.waterBlastEffect[3].effectLevel=96.593002
    dbObj.waterBlastEffect[3].damageFactor=0.053000
    dbObj.waterBlastEffect[4].effectLevel=109.523003
    dbObj.waterBlastEffect[4].damageFactor=0.056000
    dbObj.waterBlastEffect[5].effectLevel=124.130997
    dbObj.waterBlastEffect[5].damageFactor=0.059000
    dbObj.waterBlastEffect[6].effectLevel=140.634003
    dbObj.waterBlastEffect[6].damageFactor=0.062000
    dbObj.waterBlastEffect[7].effectLevel=159.281006
    dbObj.waterBlastEffect[7].damageFactor=0.067000
    dbObj.waterBlastEffect[8].effectLevel=180.358002
    dbObj.waterBlastEffect[8].damageFactor=0.071000
    dbObj.waterBlastEffect[9].effectLevel=204.195999
    dbObj.waterBlastEffect[9].damageFactor=0.077000
    dbObj.waterBlastEffect[10].effectLevel=231.184998
    dbObj.waterBlastEffect[10].damageFactor=0.083000
    dbObj.waterBlastEffect[11].effectLevel=261.792999
    dbObj.waterBlastEffect[11].damageFactor=0.091000
    dbObj.waterBlastEffect[12].effectLevel=296.588013
    dbObj.waterBlastEffect[12].damageFactor=0.100000
    dbObj.waterBlastEffect[13].effectLevel=336.286987
    dbObj.waterBlastEffect[13].damageFactor=0.111000
    dbObj.waterBlastEffect[14].effectLevel=381.821014
    dbObj.waterBlastEffect[14].damageFactor=0.125000
    dbObj.waterBlastEffect[15].effectLevel=434.455994
    dbObj.waterBlastEffect[15].damageFactor=0.143000
    dbObj.waterBlastEffect[16].effectLevel=496.026001
    dbObj.waterBlastEffect[16].damageFactor=0.167000
    dbObj.waterBlastEffect[17].effectLevel=569.390015
    dbObj.waterBlastEffect[17].damageFactor=0.200000
    dbObj.waterBlastEffect[18].effectLevel=659.484009
    dbObj.waterBlastEffect[18].damageFactor=0.250000
    dbObj.waterBlastEffect[19].effectLevel=776.106995
    dbObj.waterBlastEffect[19].damageFactor=0.333000
    dbObj.waterBlastEffect[20].effectLevel=943.422974
    dbObj.waterBlastEffect[20].damageFactor=0.500000
    dbObj.waterBlastEffect[21].effectLevel=1251.615967
    dbObj.waterBlastEffect[21].damageFactor=1.000000
    dbObj.waterBlastEffect[22].effectLevel=1614.207031
    dbObj.waterBlastEffect[22].damageFactor=2.000000
    dbObj.waterBlastEffect[23].effectLevel=2062.315918
    dbObj.waterBlastEffect[23].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*20
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=90813.953125
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=100000.000000
    dbObj.fragEffect[2].damageFactor=0.014360
    dbObj.fragEffect[3].effectLevel=300000.000000
    dbObj.fragEffect[3].damageFactor=0.024870
    dbObj.fragEffect[4].effectLevel=600000.000000
    dbObj.fragEffect[4].damageFactor=0.035170
    dbObj.fragEffect[5].effectLevel=1000000.000000
    dbObj.fragEffect[5].damageFactor=0.045400
    dbObj.fragEffect[6].effectLevel=3000000.000000
    dbObj.fragEffect[6].damageFactor=0.078640
    dbObj.fragEffect[7].effectLevel=6000000.000000
    dbObj.fragEffect[7].damageFactor=0.111220
    dbObj.fragEffect[8].effectLevel=10000000.000000
    dbObj.fragEffect[8].damageFactor=0.143580
    dbObj.fragEffect[9].effectLevel=30000000.000000
    dbObj.fragEffect[9].damageFactor=0.248690
    dbObj.fragEffect[10].effectLevel=60000000.000000
    dbObj.fragEffect[10].damageFactor=0.351700
    dbObj.fragEffect[11].effectLevel=100000000.000000
    dbObj.fragEffect[11].damageFactor=0.454040
    dbObj.fragEffect[12].effectLevel=300000000.000000
    dbObj.fragEffect[12].damageFactor=0.786410
    dbObj.fragEffect[13].effectLevel=600000000.000000
    dbObj.fragEffect[13].damageFactor=1.112160
    dbObj.fragEffect[14].effectLevel=1000000000.000000
    dbObj.fragEffect[14].damageFactor=1.435790
    dbObj.fragEffect[15].effectLevel=3000000000.000000
    dbObj.fragEffect[15].damageFactor=2.486860
    dbObj.fragEffect[16].effectLevel=6000000000.000000
    dbObj.fragEffect[16].damageFactor=3.516950
    dbObj.fragEffect[17].effectLevel=10000000000.000000
    dbObj.fragEffect[17].damageFactor=4.540360
    dbObj.fragEffect[18].effectLevel=30000001024.000000
    dbObj.fragEffect[18].damageFactor=7.864140
    dbObj.fragEffect[19].effectLevel=60000002048.000000
    dbObj.fragEffect[19].damageFactor=11.121570
    dbObj.radEffect=[pygcb.DamagePoint()]*6
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=5000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=25000.000000
    dbObj.radEffect[2].damageFactor=0.400000
    dbObj.radEffect[3].effectLevel=50000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=125000.000000
    dbObj.radEffect[4].damageFactor=5.000000
    dbObj.radEffect[5].effectLevel=250000.000000
    dbObj.radEffect[5].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*10
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.050020
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.100000
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.200000
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.399970
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=0.799980
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=1.600010
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=3.199800
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=6.399850
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=12.800050
    return dbObj
