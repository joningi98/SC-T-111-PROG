years_str = input("Years: ") # do not change this line
years_int = int(years_str) 

current_population = 307357870
secs_in_year = 31536000 

period = secs_in_year * years_int


birth = period // 7
death = period // 13
immmigration = period // 35

 

new_population = (current_population + (birth + immmigration - death))
# Missing lines here

print("New population after", years_int, " years is ", int(new_population))
