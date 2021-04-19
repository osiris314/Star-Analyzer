#Example Star
#name=KIC 8462852    quarter=16
#####################################
import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

star = input('Type Name Of Star: ')
print('\n')
search_result = lk.search_lightcurve(str(star))
print(search_result)
print('\n')
quarter_num = input('Type Number Of Quarter: ')
print(search_result[int(quarter_num)])
print('\n')

lcf = lk.search_lightcurve(str(star), quarter=quarter_num).download()
#####################################
object_name = lcf.object
origin_data = lcf.origin
telescope = lcf.telescop
instrument = lcf.instrume
date = lcf.date
raobj = lcf.ra_obj
decobj = lcf.dec_obj
equinox_data = lcf.equinox
exposure_Data = str(lcf.exposure)
#####################################
print('Name: ' + object_name)
print('Origin: ' + origin_data)
print('Telescope: ' + telescope)
print('Instrument: ' + instrument)
print('Date: ' + date)
print('Exposure: ' + exposure_Data)
print('CDPP: ' + str(lcf.estimate_cdpp()))
print('\n')
#####################################
lc = lcf.PDCSAP_FLUX.normalize()
pg = lc.to_periodogram(method="bls")
fold = lc.fold(period=pg.period_at_max_power)

print('Period at max power: {:.3f}'.format(pg.period_at_max_power))

pg.plot()
lc.plot()
fold.plot()

plt.show()
