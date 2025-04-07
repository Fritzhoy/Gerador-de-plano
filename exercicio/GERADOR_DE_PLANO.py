
#Caso 2: "init": ["computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta"]
#Caso 3: "init": ["computador-com-problema", "Computador-nao-liga"]



from gps import gps

problem = {
    #Regra 4: 
	 "init": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "ordem-de-boot-correta", "unidade-de-armazenamento-nao-integra"],
	"finish": ["troque-o-HD/SDD"],
    
	#Regra 7
    #"init": ["computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta"],
    #"finish": ["problema-processador-ou-memoria-ram"],
    
	#Regra 8
	#"init": ["computador-com-problema", "computador-liga", "a-bios-nao-inicia", "Speaker-nao-emite-alerta"],
	#"finish": ["problema-na-placa-mae"],
    
	"ops": [
    {
		"action": "Sem-problemas",
		"preconds": ["computador-com-problema","a-bios-inicia", "computador-liga", "sistema-operacional-inicia", "sistema-operacional-inicia-completamente"],
		"add": ["Sem-problemas"],
		"delete": ["computador-com-problema"]
	},
    {
		"action": "sistema-operacional-corrompido",
		"preconds": ["computador-com-problema", "a-bios-inicia", "computador-liga", "sistema-operacional-inicia", "sistema-operacional-nao-inicia-completamente"],
		"add": ["sistema-operacional-corrompido"],
		"delete": ["computador-com-problema"]
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
		"action": "unidade-de-armazenamento-detectada",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "checar-unidade-armazenamento"],
		"add": ["checar-ordem-boot"],
		"delete": ["checar-unidade-armazenamento"]
	},
    {
		"action": "ordem-de-boot-correta",
		"preconds": ["computador-com-problema", "computador-liga", "a-bios-inicia", "sistema-operacional-nao-inicia", "unidade-de-armazenamento-detectada", "checar-ordem-boot", "ordem-de-boot-correta"],
		"add": ["checar-unidade-de-armazenamento-integra"],
		"delete": ["checar-ordem-boot"]
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
		"preconds": ["computador-com-problema", "Computador-nao-liga"],
		"add": ["checar-fonte"],
		"delete": [" "]
	},
    {
		"action": "a-fonte-inicia",
		"preconds": ["Computador-nao-liga", "checar-fonte"],
		"add": ["fonte-inicia", "checar-voltagem"],
		"delete": ["checar-fonte"]
	},
    {
		"action": "a-fonte-nao-inicia",
		"preconds": ["Computador-nao-liga", "fonte-nao-inicia"],
		"add": ["checar-alimentcao"],
		"delete": [" "]
	},
    {
		"action": "Voltagem-esta-correta",
		"preconds": ["computador-com-problema", "Computador-nao-liga", "fonte-inicia", "checar-voltagem", "Voltagem-correta"],
		"add": ["checar-circuito-alimentacao"],
		"delete": ["checar-voltagem"]
	},
    {
		"action": "checar-circuito-de-alimentacao",
		"preconds": ["computador-com-problema", "Computador-nao-liga", "fonte-inicia", "Voltagem-correta"],
		"add": ["circuito-de-alimentacao"],
		"delete": [" "]
	},
    {
		"action": "Problema-no-circuito-de-alimentacao-da-placa-mae",
		"preconds": ["computador-com-problema", "Computador-nao-liga", "fonte-inicia", "Voltagem-correta", "circuito-de-alimentacao"],
		"add": ["Problema-detectado"],
		"delete": ["computador-com-problema"]
	},
	{
		"action": "o-computador-esta-ligado-na-tomada",
		"preconds": ["computador-nao-liga","fonte-nao-inicia", "alimentacao-nao-conectada"],
		"add": ["computador-liga"],
		"delete": ["computador-nao-liga", "fonte-nao-inicia", "alimentacao-nao-conectada"]
	},
    {
		"action": "fonte-inicia",
		"preconds": ["computador-nao-liga", "fonte-nao-inicia"],
		"add": ["alimentacao-conectada"],
		"delete": [""]
	},
    {
		"action": "alimentacao-conectada",
		"preconds": ["computador-nao-liga", "fonte-nao-inicia"],
		"add": ["alimentacao-nao-conectada"],
		"delete": [""]
	},
	 {
		"action": "checar-se-o-computador-liga",
		"preconds": ["computador-com-problema", "Computador-nao-liga"],
		"add": ["fonte-inicia"],
		"delete": [" "]
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
