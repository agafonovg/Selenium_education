# a = 60
# b = 60*a
# second_per_hours = b
# second_per_day = second_per_hours*24
# c = second_per_day/second_per_hours
# d = second_per_day//second_per_hours
# print (second_per_hours)
# print (second_per_day)
# print (c)
# print (d)

# year_list = [1992, 1993, 1994, 1995, 1996, 1997]

# things = ['mozzarella', 'Cinderella', 'salmonella']
# things[1] = 'CINDERELLA'
# print (things)
# del things[2]
# print (things)
# things.remove("mozzarella")
# print (things)
# things.pop()
# print (things)
# surprise = ["Groucho", 'Chico', 'Harpo']
# a = surprise[2].lower()
# surprise[2] = a
# print (surprise)
# b = a.upper()
# surprise[2] = b
# print (surprise)

# e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
# # print (e2f['walrus'])
# f2e = dict(map(reversed, e2f.items()))
# print (f2e)
# print (f2e['chien'])
# print (list(e2f.values()))


# life = {
# 	'animals': {'cats':['Henry', 'Grumpy', 'Lucy'], 'octopi':[], 'emus':[] },
# 	'plants': [],
# 	'other':[]
# }
# # print (life.keys())
# # print (life['animals'].keys())
# print (life['animals']['cats'])
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))