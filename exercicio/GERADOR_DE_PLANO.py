
from gps import gps

problem = {
    #Regra1:
    #"init": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-inicia", "sistema-operacional-inicia-completamente"],
    #"finish": ["Operando-normalmente"],
    
	#Regra 2:
    #"init": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-inicia", "sistema-operacional-nao-inicia-completamente"],
    #"finish": ["sistema-operacional-corrompido"],
    
	#Regra 3: 
    
	#"init": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-inicia", "sistema-operacional-nao-inicia-completamente"],
    #"finish": ["sistema-operacional-corrompido"],
    
	#Regra 4: 
	"init": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "ordem-de-boot-correta", "unidade-de-armazenamento-nao-integra"],
	"finish": ["troque-o-HD/SDD"],
    
	#Regra 5: 
    #"init": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "ordem-de-boot-nao-esta-correta"],
    #"finish": ["Ajustar-Boot"],

	#Regra 6: 
    #"init": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-nao-detectada"],
    #"finish": ["HD-desconectado-ou-com-problema"],
    
	#Regra 7
    #"init": ["computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta"],
    #"finish": ["problema-processador-ou-memoria-ram"],
    
	#Regra 8
	#"init": ["computador-com-problema", "computador-liga", "a-bios-nao-inicia", "Speaker-nao-emite-alerta"],
	#"finish": ["problema-na-placa-mae"],
    
	#Regra 9
    #"init": ["computador-com-problema", "computador-nao-liga", "fonte-inicia", "voltagem-correta"],
	#"finish": ["problema-no-circuito-da-placa-mae"],
    
	#Regra 10
    #"init": ["computador-com-problema", "computador-nao-liga", "fonte-inicia", "voltagem-nao-esta-correta"],
	#"finish": ["fonte-esta-com-problema"],
    
    #Regra 11
    #"init": ["computador-com-problema", "computador-nao-liga", "fonte-nao-inicia", "alimentacao-conectada"],
	#"finish": ["fonte-esta-queimada"],
    
	#Regra 12
    #"init": ["computador-com-problema", "computador-nao-liga", "fonte-nao-inicia", "alimentacao-nao-conectada"],
	#"finish": ["ligar-na-tomada"],
    
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
		"add": ["Ajustar-Boot"],
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

def main():
    start = problem['init']
    finish = problem['finish']
    ops = problem['ops']
    msg = 'Deve-se executar:  '
    plan = gps(start, finish, ops, msg)
    if plan is not None:
        for action in plan:
            print (action)
    else:
        print('O plano não foi gerado')

if __name__ == '__main__':
    main()
