def solution(video_len, pos, op_start, op_end, commands):
    cmd = {
        "prev": -10,
        "next": 10
    }
    
    video_len = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    pos = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    op_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    op_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
        
    if op_start <= pos and pos <= op_end:
            pos = op_end
        
    for c in commands:
        pos += cmd[c]
        
        if pos < 0:
            pos = 0
        elif pos > video_len:
            pos = video_len
            
        if op_start <= pos and pos <= op_end:
            pos = op_end
            
    m = pos // 60
    s = pos % 60
    
    answer = str(m).zfill(2)+":"+str(s).zfill(2)
    
    return answer