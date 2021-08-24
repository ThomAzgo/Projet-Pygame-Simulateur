import json


class Gamelvl:

    def printPhrase(self,phrase,dico,morceau):
        listChoix=[]
        if dico["cas"][phrase]["typeAction"]==1:
            for choix in dico["cas"][phrase]["Choix"]:
                listChoix.append(dico["cas"][phrase]["Choix"][choix])
        
        elif dico["cas"][phrase]["typeAction"]==2:
            for choix in dico["cas"][phrase][morceau]:
                listChoix.append(dico["cas"][phrase][morceau][choix][0])

        return listChoix
    def printPhrasePNJ(self,phrase,dico):
        var=dico["cas"][phrase]["phrasePNJ"]
        return var
    def Output(self,phrase,morceau,dico,case):
        case=str(case)
        if dico["cas"][phrase]["typeAction"]==1:
            point = dico["cas"][phrase]["reponse"]["reponse"+case][2]
            humeur =dico["cas"][phrase]["reponse"]["reponse"+case][3] 
            phrase=dico["cas"][phrase]["reponse"]["reponse"+case][1]
            morceau="morceau1"
            

        elif dico["cas"][phrase]["typeAction"]==2:
            if dico["cas"][phrase][morceau]["Choix"+case][1]=="stop":
                point = dico["cas"][phrase][morceau]["Choix"+case][2]
                humeur =dico["cas"][phrase]["reponse"]["reponse"+case][2] 
                phrase = dico["cas"][phrase]["reponse"]["reponse"+case][1]
                morceau="morceau1"
                
            else :
                point = dico["cas"][phrase][morceau]["Choix"+case][2]
                humeur =dico["cas"][phrase]["reponse"]["reponse"+case][2] 
                phrase = phrase
                morceau = dico["cas"][phrase][morceau]["Choix"+case][1]
                

        return phrase,morceau,point,humeur


    def savepoint(self,point,niveau):
        print(point) 
        if point>=800:
            star=3
        elif point>=600:
            star=2
        elif point>=400:
            star=1
        else :
            star=0
        with open("listeLVL.json", 'r+') as file :
            data = json.load(file)

            if data[niveau]>=star:
                pass
            else :
                data[niveau] = star

        with open("listeLVL.json", 'w') as file:
            json.dump(data, file, indent=4)

