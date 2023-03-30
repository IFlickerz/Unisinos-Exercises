def notasMedia(a,b,c):
    if a >= 0 and b >= 0 and c >= 0:
        media = (a + b + c) / 3
        if media <= 4:
            return "D"
        elif media <= 7:
            return "C"
        elif media <= 9:
            return "B"
        else:
            return "A"
    return "ERRO"

print(notasMedia(9,10,9))
    
