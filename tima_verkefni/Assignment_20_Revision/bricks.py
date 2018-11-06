def check_bricks(small, large, goal):
    return (goal % 5) <= small and small >= (goal - (large * 5))