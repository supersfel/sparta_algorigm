current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def rotate_to_left(d):
    return (d+3) % 4

def go_back(d):
    return (d+2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):

    n = len(room_map)
    m = len(room_map[0])
    room_map[r][c] = 2
    count =1
    queue = [[r,c,d]]

    while queue:
        r,c,d = queue.pop(0)
        temp_d = d


        for i in range(4):
            temp_d = rotate_to_left(temp_d)
            new_r = r + dr[temp_d]
            new_c = c + dc[temp_d]

            if room_map[new_r][new_c] == 0:
                count +=1
                room_map[new_r][new_c] = 2
                queue.append([new_r,new_c,temp_d])
                break #???

            elif i == 3:

                temp_d = go_back(temp_d)
                new_r, new_c = r + dr[temp_d], c + dc[temp_d]
                queue.append([new_r,new_c,d])   #왜 여기가 d가 들어가야 하지? << 그래야 프로그램이 끝난다?!?
                # 서,남,동을 확인 한담에 결국 첫위치로 돌아오기때문에 고정된 d가 필요하다!

                if room_map[new_r][new_c] == 1:
                    return count




# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))