def bouncing_ball(h, bounce, window):
    times = 1
    if h <= 0 or 1 <= bounce or bounce <= 0 or h <= window:
        return -1
    bounce_h = bounce * h
    h = bounce_h
    while h > 0 and 0 < bounce < 1 and window < h:
        bounce_h = bounce * h
        times = times + 2
        h = bounce_h

    return times


print(bouncing_ball(3, 1, 1.5))
