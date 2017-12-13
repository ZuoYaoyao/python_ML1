def get_movie_url(category, location):
    url = 'https://movie.douban.com/tag/#/?tags=电影,'
    # append args
    url = url + category + ',' + location
    return url


print(get_movie_url('剧情', '美国'))
