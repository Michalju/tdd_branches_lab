def latest(scores):
    return scores[-1]


def personal_best(scores):
        return max(scores)


def personal_top_three(scores):
    scores_local = scores.copy()
    personal_top_three=[]

   
    index = 0
    while len(scores_local) and index<3:
        
        personal_top_three.append(max(scores_local))

        scores_local.remove(max(scores_local))

        index +=1

    print(personal_top_three)
    return personal_top_three
    