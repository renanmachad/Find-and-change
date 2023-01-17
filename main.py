# Author : Renan Machado



import os


filepath= "VIEWS"
path = os.listdir(filepath)
current = "CASSOL_APP"
new_string= "RUB_INTEGRACAO"

cassol_index="CASSOL_INDEX"
new_index="TERCEIROS_INDEX"

cassol_data= "CASSOL_DATA"
new_data= "TERCEIROS_DATA"


class Refactor:

    
    def gen_grant_access(self) ->None:
        
        return None



    def change_words_in_file(self)->None:
        for content in path:
            counter =0
            print("CONTENT: "+content)
            if not content.endswith(".py"):
                try:
                    with open(filepath+"/"+content,"r",encoding="utf-8") as file:
                        result = file.read()
                        counter = result.count(current)
                        result= result.replace(current,new_string)
                        result= result.replace(cassol_index,new_index)
                        result=result.replace(cassol_data,new_data)
                except:
                    print("Cannot read the file")
                    pass
                else:
                    with open(filepath+"/"+content,"w",encoding="utf-8") as newfile:
                        newfile.write(result)
                        total=0
                        print(content,":",counter," changes")
                        total+=1
                        print(f"Totally {total} files changed")




if __name__=="__main__":
    refactor =Refactor()
    refactor.change_words_in_file()
