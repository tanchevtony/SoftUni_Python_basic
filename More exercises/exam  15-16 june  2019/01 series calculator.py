movie_name = input()
series = int(input())
episodes = int(input())
episode_time = float(input())  # without adverts

adverts_per_episode = episode_time * 0.20
episode_with_adverts = episode_time + adverts_per_episode
special_time = series * 10

total_time = int(episode_with_adverts * episodes * series + special_time)
print(f"Total time needed to watch the {movie_name} series is {total_time} minutes.")