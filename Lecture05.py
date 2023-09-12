# coding: utf-8
print("hello world")
foo=["a","b"]
get_ipython().run_line_magic('save', 'mycode')
foo2=["b","a"]
foo==foo2
foo2.sort()
foo2
foo==foo2
animals = {'dog','cat'}
type(animals)
animals2={'cat','dog'}
animals2
animals==animals2
animals.add('turtle')
animals
animals2.add('fish')
animals2
animals.union(animals2)
animals.intersection(animals2)
animals3={'cow'}
animals2.intersect(animals3)
animals2.intersection(animals3)
print(animals2.intersection(animals3))
set(['a','b'])
list(set(['a','b']))
list(set(['a','b','b','c']))
animal_legs = {'dog':4,'ant':6}
animal_legs['dog']
animal_legs['ant']
animal_legs['spider']
animal_legs['spider']=8
animal_legs['spider']
animal_legs.keys()
set(animal_legs.key())
set(animal_legs.keys())
animal_legs.values()
animals
legs=[4,4,4]
animal_legs_data = [('cat',4),('dog',4),('turtle',4)]
dict(animal_leg_data)
dict(animal_legs_data)
zip(animals,legs)
list(zip(animals,legs))
dict(list(zip(animals,leg)))
dict(list(zip(animals,legs)))
dict(zip(animals,legs))
animal_legs.items()
for thing in animal_legs:
    print(thing)
    
for thing in animal_legs:
    print("animal: ", thing, "value: ", animal_legs[thing])
    
for thing in animal_legs:
    print("animal: ", thing, "legs: ", animal_legs[thing])
    
for key, value in animal_legs.items():
    print("animal: ",key,"legs: ",value)
    
data = ({"animal':'dog','legs':4},{'animal:'cat','legs':4},{'animals':'bob','legs':2},]
data = ({'animal':'dog','legs':4},{'animal:'cat','legs':4},{'animals':'bob','legs':2},]
data = ({'animal':'dog','legs':4},{'animal:'cat','legs':4},{'animals':'bob','legs':2}]
data2 = {'animals':['dog','cat','bob'],'legs':[4,4,2]}
data = [{'animal':'dog','legs':4},{'animal:'cat','legs':4},{'animals':'bob','legs':2}]
data = [{'animal':'dog','legs':4},{'animal:'cat','legs':4},{'animals':'bob','leg':2}]
data = [{'animal':'dog','legs':4},{'animal':'cat','legs':4},{'animals':'bob','leg':2}]
data
