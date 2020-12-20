def solution(skill, skill_trees):
    answer = 0
    skills = {}
    for i in range(len(skill)):
        skills[skill[i]] = i
    for tree in skill_trees:
        trees = []
        for t in range(len(tree)):
            if tree[t] in skill:
                trees.append([tree[t], skills[tree[t]]])
        
        for t in range(len(trees)):
            if trees[t][1] != t:
                break
        else:
            answer += 1
    
                        
    return answer