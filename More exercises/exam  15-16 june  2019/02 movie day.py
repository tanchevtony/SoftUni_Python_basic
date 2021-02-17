import math

pictures_time = int(input())
number_of_scene = int(input())
time_per_scene = int(input())

preparation = pictures_time * 0.15
time_for_all_scene = number_of_scene * time_per_scene
needed_time = time_for_all_scene + preparation
diff = math.ceil(abs(pictures_time - needed_time))
if pictures_time >= needed_time:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")