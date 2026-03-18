media_minima = 6
total_notas = 4

def calcular_media(notas):
    if notas:
        return sum(notas)/4
    return 0
    

def status_escolar(notas):
    if len(notas) == 4:
        media = calcular_media(notas)
        if media >= media_minima:
            return "Aprovado"
        elif (media_minima - 2) <= media < media_minima:
            return "Recuperação"
        else:
            return "Reprovado"
    else:
        return "Em andamento"

def objetivo_ou_final(notas):   
    faltam = total_notas - len(notas)
    media_alvo_total = media_minima * total_notas
    soma_atual = sum(notas) if notas else 0

    if faltam == 0:
        return {"média": calcular_media(notas)}
    
    elif faltam == 1:
        if sum(notas) > 24:
            return{"Objetivo": "Não zerar a prova"}
        return {"Nota alvo": media_alvo_total - soma_atual}
    
    elif faltam == 2:
        nota_alvo = (media_alvo_total - soma_atual)/2
        return {"Notas alvo nos 2 B. restantes": nota_alvo}
    
    else:
        return {"Objetivo": "Estudar"}  
    