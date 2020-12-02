def solution(s, n):
    answer = ''
    if n >= 26:
        n = n%26
    for word in s:
        if word == ' ':
            answer += ' '
        elif ord('A') <= ord(word) <= ord('Z'):
            if ord(word) + n > ord('Z'):
                answer += chr(ord(word) + n - 26)
            else:
                answer += chr(ord(word) + n)
        else:
            if ord(word) + n > ord('z'):
                answer += chr(ord(word) + n - 26)
            else:
                answer += chr(ord(word) + n)
    
    return answer
