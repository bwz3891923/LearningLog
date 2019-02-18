from die import Die
import pygal


die_1 = Die()
die_2 = Die()
die_3 = Die()
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()+die_3.roll()
    results.append(result)

frequencies=[]
for value in range(1,die_1.num_sides+die_2.num_sides+die_3.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

loops=[]
for loop in range(1,die_1.num_sides+die_2.num_sides+die_3.num_sides+1):
    loops.append("%i"%loop)



hist=pygal.Bar()
hist.title="Results of rolling one D6 1000 times"
hist.x_labels=loops
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D8+D8',frequencies)
hist.render_to_file('die_visual.svg')



print(frequencies)
