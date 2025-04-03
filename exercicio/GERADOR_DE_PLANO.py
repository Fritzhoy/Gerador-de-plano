#Caso 1: "init": ["Computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta"]
#Caso 2: "init": ["Computador-com-problema", "Computador-nao-liga"]
#Caso 3: "init": ["Computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-nao-emite-alerta"]

from gps import gps

problem = {
	"init": ["Computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta"],
	"finish": ["Problema-detectado"],
	"ops": [
	{
		"action": "Problema-na-placa-mae",
		"preconds": ["Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "Speaker-nao-emite-alerta", "Problema-na-placa-mae"],
		"add": ["Problema-detectado"],
		"delete": ["computador-com-problema"]
	},
    {
		"action": "Problema-processador-e-memoria-ram",
		"preconds": ["Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta", "Problema-processador-e-memoria"],
		"add": ["Problema-detectado"],
		"delete": ["computador-com-problema"]
	},
    {
		"action": "a-bios-nao-esta-iniciando",
		"preconds": ["Computador-com-problema", "Computador-liga", "checar-bios", "a-bios-nao-inicia"],
		"add": ["checar-speaker"],
		"delete": ["checar-bios"]
	},
    {
		"action": "Speaker-nao-emite-alerta",
		"preconds": ["Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "checar-speaker", "Speaker-nao-emite-alerta"],
		"add": ["Problema-na-placa-mae"],
		"delete": [" "]
	},
    {
		"action": "Speaker-emite-alerta",
		"preconds": ["Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "checar-speaker", "Speaker-emite-alerta"],
		"add": ["Problema-processador-e-memoria"],
		"delete": [" "]
	},
    {
		"action": "o-computador-liga",
		"preconds": ["Computador-com-problema", "checar-computador-liga"],
		"add": ["Computador-liga", "checar-bios"],
		"delete": ["checar-computador-liga"]
	},
    {
		"action": "o-computador-nao-liga",
		"preconds": ["Computador-com-problema", "Computador-nao-liga"],
		"add": ["checar-fonte"],
		"delete": [" "]
	},
    {
		"action": "checar-se-a-fonte-inicia",
		"preconds": ["Computador-nao-liga", "checar-fonte"],
		"add": ["fonte-inicia", "checar-voltagem"],
		"delete": [" "]
	},
    {
		"action": "a-fonte-nao-inicia",
		"preconds": ["Computador-nao-liga", "fonte-nao-inicia"],
		"add": ["checar-alimentcao"],
		"delete": [" "]
	},
    {
		"action": "checar-se-voltagem-esta-correta",
		"preconds": ["Computador-com-problema", "Computador-nao-liga", "fonte-inicia", "checar-voltagem"],
		"add": ["Voltagem-correta"],
		"delete": ["checar-voltagem"]
	},
    {
		"action": "checar-circuito-de-alimentacao",
		"preconds": ["Computador-com-problema", "Computador-nao-liga", "fonte-inicia", "Voltagem-correta"],
		"add": ["circuito-de-alimentacao"],
		"delete": [" "]
	},
    {
		"action": "Problema-no-circuito-de-alimentacao-da-placa-mae",
		"preconds": ["Computador-com-problema", "Computador-nao-liga", "fonte-inicia", "Voltagem-correta", "circuito-de-alimentacao"],
		"add": ["Problema-detectado"],
		"delete": ["Computador-com-problema"]
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
		"preconds": ["Computador-com-problema", "Computador-nao-liga"],
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
