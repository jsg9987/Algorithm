def solution(n, build_frame):
    # 기둥과 보 저장을 위한 set
    structures = set()

    # 기둥 설치 가능 여부 체크
    def can_install_pillar(x, y):
        return y == 0 or (x, y - 1, 0) in structures or (x - 1, y, 1) in structures or (x, y, 1) in structures

    # 보 설치 가능 여부 체크
    def can_install_beam(x, y):
        return (x, y - 1, 0) in structures or (x + 1, y - 1, 0) in structures or ((x - 1, y, 1) in structures and (x + 1, y, 1) in structures)

    # 구조물 유지 가능 여부 체크
    def is_valid():
        for x, y, a in structures:
            if a == 0 and not can_install_pillar(x, y):
                return False
            if a == 1 and not can_install_beam(x, y):
                return False
        return True

    # 명령어 실행
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            structures.add((x, y, a))
            if not is_valid():
                structures.remove((x, y, a))
        else:  # 삭제
            structures.remove((x, y, a))
            if not is_valid():
                structures.add((x, y, a))

    # 정렬 후 반환
    return sorted(structures, key=lambda structure: (structure[0], structure[1], structure[2]))
