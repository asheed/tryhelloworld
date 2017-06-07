people = 3  # 사람 수
apple = 20  # 사과 수

if people < apple / 5:
    # 한사람이 배터지게 사과를 먹으려면 5개는 먹어야 함.
    print('신나는 사과 파티! 배 터지게 먹기')

if apple % people > 0:
    # 사과수를 사람수로 나누었을 때, 나머지가 0보다 크면
    # 즉, 딱 맞아떨어지지 않으면..
    print('사과 수가 맞지 않아! 몇 개는 쪼개 먹자!')

if people > apple:
    print('사람이 너무 많아! 몇 명은 못 먹겠네...')