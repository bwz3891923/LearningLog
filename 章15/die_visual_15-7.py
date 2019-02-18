from die import Die
import pygal


die_1 = Die(8)
die_2 = Die(8)
results=[]
for roll_num in range(100000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

frequencies=[]
for value in range(1,die_1.num_sides+die_2.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

loops=[]
for loop in range(1,die_1.num_sides+die_2.num_sides+1):
    loops.append("%i"%loop)



hist=pygal.Bar()
hist.title="Results of rolling one D6 1000 times"
hist.x_labels=loops
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D8+D8',frequencies)
hist.render_to_file('die_visual.svg')



print(frequencies)
