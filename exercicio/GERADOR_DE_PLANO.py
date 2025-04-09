
from gps import gps


problem = {
    
	"ops": [
    {
		"action": "sistema-operacional-inicia-completamente",
		"preconds": ["computador-com-problema", "a-bios-inicia", "computador-liga", "sistema-operacional-inicia", "checar-sistema-operacional-inicia-completamente", "sistema-operacional-inicia-completamente"],
		"add": ["Operando-normalmente"],
		"delete": ["computador-com-problema", "checar-sistema-operacional-inicia-completamente"]
	},
    {
		"action": "sistema-operacional-nao-inicia-completamente",
		"preconds": ["computador-com-problema", "a-bios-inicia", "computador-liga", "sistema-operacional-inicia", "checar-sistema-operacional-inicia-completamente", "sistema-operacional-nao-inicia-completamente"],
		"add": ["sistema-operacional-corrompido"],
		"delete": ["computador-com-problema", "checar-sistema-operacional-inicia-completamente"]
	},
    {
		"action": "a-bios-inicia",
		"preconds": ["computador-com-problema", "computador-liga", "checar-bios", "a-bios-inicia"],
		"add": ["checar-OS"],
		"delete": ["checar-bios"]
	},
    {
		"action": "a-bios-nao-inicia",
		"preconds": ["computador-com-problema", "computador-liga", "checar-bios", "a-bios-nao-inicia"],
		"add": ["checar-speaker"],
		"delete": ["checar-bios"]
	},
    {
		"action": "sistema-operacional-nao-inicia",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "checar-OS", "sistema-operacional-nao-inicia"],
		"add": ["checar-unidade-armazenamento"],
		"delete": ["checar-OS"]
	},
    {
		"action": "sistema-operacional-inicia",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "checar-OS", "sistema-operacional-inicia"],
		"add": ["checar-sistema-operacional-inicia-completamente"],
		"delete": ["checar-OS"]
	},
    {
		"action": "unidade-de-armazenamento-detectada",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "checar-unidade-armazenamento"],
		"add": ["checar-ordem-boot"],
		"delete": ["checar-unidade-armazenamento"]
	},
    {
		"action": "unidade-de-armazenamento-nao-detectada",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-nao-detectada", "checar-unidade-armazenamento"],
		"add": ["HD-desconectado-ou-com-problema"],
		"delete": ["computador-com-problema", "checar-unidade-armazenamento"]
	},
    {
		"action": "ordem-de-boot-correta",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "checar-ordem-boot", "ordem-de-boot-correta"],
		"add": ["checar-unidade-de-armazenamento-integra"],
		"delete": ["checar-ordem-boot"]
	},
    {
		"action": "ordem-de-boot-nao-esta-correta",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "checar-ordem-boot", "ordem-de-boot-nao-esta-correta"],
		"add": ["ajustar-boot"],
		"delete": ["computador-com-problema", "checar-ordem-boot"]
	},
    {
		"action": "unidade-de-armazenamento-nao-integra",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "ordem-de-boot-correta", "checar-unidade-de-armazenamento-integra", "unidade-de-armazenamento-nao-integra"],
		"add": ["troque-o-HD/SDD"],
		"delete": ["checar-unidade-de-armazenamento-integra", "computador-com-problema"]
	},
    {
		"action": "Speaker-nao-emite-alerta",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-nao-inicia", "checar-speaker", "Speaker-nao-emite-alerta"],
		"add": ["problema-na-placa-mae"],
		"delete": ["computador-com-problema", "checar-speaker"]
	},
    {
		"action": "Speaker-emite-alerta",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-nao-inicia", "checar-speaker", "Speaker-emite-alerta"],
		"add": ["problema-processador-ou-memoria-ram"],
		"delete": ["computador-com-problema", "checar-speaker"]
	},
    {
		"action": "o-computador-liga",
		"preconds": ["computador-com-problema", "computador-liga"],
		"add": ["checar-bios"],
		"delete": ["checar-computador-liga"]
	},
    {
		"action": "o-computador-nao-liga",
		"preconds": ["computador-com-problema", "computador-nao-liga"],
		"add": ["checar-fonte"],
		"delete": [" "]
	},
    {
		"action": "fonte-inicia",
		"preconds": ["computador-nao-liga", "checar-fonte","fonte-inicia"],
		"add": ["checar-voltagem"],
		"delete": ["checar-fonte"]
	},
    {
		"action": "fonte-nao-inicia",
		"preconds": ["computador-com-problema", "computador-nao-liga", "checar-fonte",  "fonte-nao-inicia"],
		"add": ["checar-alimentacao"],
		"delete": ["checar-fonte"]
	},
    {
		"action": "voltagem-correta",
		"preconds": ["computador-com-problema", "computador-nao-liga", "fonte-inicia",  "checar-voltagem", "voltagem-correta"],
		"add": ["problema-no-circuito-da-placa-mae"],
		"delete": ["computador-com-problema", "checar-voltagem"]
	},
    {
		"action": "voltagem-nao-esta-correta",
		"preconds": ["computador-com-problema", "computador-nao-liga", "fonte-inicia",  "checar-voltagem", "voltagem-nao-esta-correta"],
		"add": ["fonte-esta-com-problema"],
		"delete": ["computador-com-problema", "checar-voltagem"]
	},
    {
		"action": "alimentacao-conectada",
		"preconds": ["computador-com-problema", "computador-nao-liga", "fonte-nao-inicia", "checar-alimentacao", "alimentacao-conectada"],
		"add": ["fonte-esta-queimada"],
		"delete": ["computador-com-problema", "checar-alimentacao"]
	},
    
    {
		"action": "alimentacao-nao-conectada",
		"preconds": ["computador-com-problema", "computador-nao-liga", "fonte-nao-inicia", "checar-alimentacao", "alimentacao-nao-conectada"],
		"add": ["ligar-na-tomada"],
		"delete": ["computador-com-problema", "checar-alimentacao"]
	}, 
	]
}
def Lista_Problemas():
    print("================================================================================")
    print("\nLista de Problemas:\n")
    print("1 - Operando-normalmente")
    print("2 - Sistema operacional corrompido")
    print("3 - Troque o HD/SDD")
    print("4 - Ajustar boot")
    print("5 - HD desconectado ou com problema")
    print("6 - Problema no processador ou memória RAM")
    print("7 - Problema na placa mãe")
    print("8 - Problema no circuito da placa mãe")
    print("9 - Fonte está com problema")
    print("10 - Fonte está queimada")
    print("11 - Ligar na tomada")
    print("\n================================================================================\n")

    escolha = input("Escolha o número do problema que deseja simular: ")
    
    
    problemas = {
        "1": (["computador-com-problema", "computador-liga", "a-bios-inicia",
               "sistema-operacional-inicia", "sistema-operacional-inicia-completamente"],
              ["Operando-normalmente"]),

        "2": (["computador-com-problema", "computador-liga", "a-bios-inicia",
               "sistema-operacional-inicia", "sistema-operacional-nao-inicia-completamente"],
              ["sistema-operacional-corrompido"]),

        "3": (["computador-com-problema", "computador-liga", "a-bios-inicia",
               "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada",
               "ordem-de-boot-correta", "unidade-de-armazenamento-nao-integra"],
              ["troque-o-HD/SDD"]),

        "4": (["computador-com-problema", "computador-liga", "a-bios-inicia",
               "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada",
               "ordem-de-boot-nao-esta-correta"],
              ["ajustar-boot"]),

        "5": (["computador-com-problema", "computador-liga", "a-bios-inicia",
               "sistema-operacional-nao-inicia", "unidade-de-armazenamento-nao-detectada"],
              ["HD-desconectado-ou-com-problema"]),

        "6": (["computador-com-problema", "checar-computador-liga",
               "a-bios-nao-inicia", "Speaker-emite-alerta"],
              ["problema-processador-ou-memoria-ram"]),

        "7": (["computador-com-problema", "computador-liga",
               "a-bios-nao-inicia", "Speaker-nao-emite-alerta"],
              ["problema-na-placa-mae"]),

        "8": (["computador-com-problema", "computador-nao-liga",
               "fonte-inicia", "voltagem-correta"],
              ["problema-no-circuito-da-placa-mae"]),

        "9": (["computador-com-problema", "computador-nao-liga",
               "fonte-inicia", "voltagem-nao-esta-correta"],
              ["fonte-esta-com-problema"]),

        "10": (["computador-com-problema", "computador-nao-liga",
                "fonte-nao-inicia", "alimentacao-conectada"],
               ["fonte-esta-queimada"]),

        "11": (["computador-com-problema", "computador-nao-liga",
                "fonte-nao-inicia", "alimentacao-nao-conectada"],
               ["ligar-na-tomada"]),
    }
    print("\n================================================================================\n")

    if escolha in problemas:
        return problemas[escolha]
    else:
        print("Opção inválida.")
        exit(1)

def main():

    start, finish = Lista_Problemas()
    ops = problem['ops']
    msg = 'Deve-se executar:  '
    plan = gps(start, finish, ops, msg)
    if plan is not None:
        for action in plan:
            print (action)
    else:
        print('O plano não foi gerado')
    print("\n================================================================================\n")
if __name__ == '__main__':
    main()
