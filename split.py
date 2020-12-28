# A codewars solution for one of the challenges. I prefer working it out in VSC.

def solution(s):
    answer = []
    for x in range(0,len(s),2):
        try:
            answer.append(s[x] + s[x+1])
        except:
            answer.append(s[x] + '_')
    print(answer)
    return answer

solution("asdfadsf") # ['as', 'df', 'ad', 'sf']
solution("asdfads")   # ['as', 'df', 'ad', 's_']
solution("abc")       # ['ab', 'c_']
solution("")         # []
solution("x")        # ["x_"]