from pyecharts.faker import Faker

print(Faker.values())
print(Faker.choose())

i = zip(Faker.choose(), Faker.values())
print(i)
