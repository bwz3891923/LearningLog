import pygal

wm=pygal.Worldmap()
wm.title='Population of Countries in North Amercia'
wm.add('North Amercia',{'ca':3412600,'us':309349000,'mx':113423000})
wm.render_to_file('na_populations.svg')
