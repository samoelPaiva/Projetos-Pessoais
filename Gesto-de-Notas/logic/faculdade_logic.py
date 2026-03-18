media_minima = 7
total_notas = 3

def calcular_media(notas):
    if notas:
        return sum(notas)/3
    return 0

def status_universitario(notas):
    if len(notas) == 3:
        media = calcular_media(notas)
        if media >= media_minima:
            return "Aprovado"
        elif (3) <= media < media_minima:
            return "Quarta Prova"
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
        nota_alvo = media_alvo_total - soma_atual
        return {"Nota alvo": round(nota_alvo)}
    
    elif faltam == 2:
        nota_alvo = (media_alvo_total - soma_atual)/2
        return {"Notas alvo nas 2 Uni. restantes": round(nota_alvo, 2)}

    else:
        return {"Objetivo": "Estudar muito"}
 