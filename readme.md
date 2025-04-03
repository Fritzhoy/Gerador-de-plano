## Estado Inicial

## Caso 1

- **Init:** "Computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-nao-emite-alerta"

### Ação: "o-computador-liga"

- **Requisitos:** "Computador-com-problema", "checar-computador-liga"
- **Adiciona:** "Computador-liga", "checar-bios"
- **Remove:** "checar-computador-liga"

### Ação: "a-bios-nao-esta-iniciando"

- **Requisitos:** "Computador-com-problema", "Computador-liga", "checar-bios", "a-bios-nao-inicia"
- **Adiciona:** "checar-speaker"
- **Remove:** "checar-bios"

### Ação: "Speaker-nao-emite-alerta"

- **Requisitos:** "Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "checar-speaker", "Speaker-nao-emite-alerta"
- **Adiciona:** "Problema-na-placa-mae"
- **Remove:** -

### Ação: "Problema-na-placa-mae"

- **Requisitos:** "Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "Speaker-nao-emite-alerta", "Problema-na-placa-mae"
- **Adiciona:** "Problema-detectado"
- **Remove:** "Computador-com-problema"

## Caso 2: 

- **init:** "Computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta"

### Ação: "o-computador-liga"

- **Requisitos:** "Computador-com-problema", "checar-computador-liga"
- **Adiciona:** "Computador-liga", "checar-bios"
- **Remove:** "checar-computador-liga"

### Ação: "a-bios-nao-esta-iniciando"

- **Requisitos:** "Computador-com-problema", "Computador-liga", "checar-bios", "a-bios-nao-inicia"
- **Adiciona:** "checar-speaker"
- **Remove:** "checar-bios"

### Ação: "Speaker-emite-alerta"

- **Requisitos:** "Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "checar-speaker", "Speaker-emite-alerta"
- **Adiciona:** "Problema-processador-e-memoria"
- **Remove:** -

### Ação: "Problema-processador-e-memoria-ram"

- **Requisitos:** "Computador-com-problema", "Computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta", "Problema-processador-e-memoria"
- **Adiciona:** "Problema-detectado"
- **Remove:** "Computador-com-problema"



## Caso 3

- **Init:** "Computador-com-problema", "Computador-nao-liga"

### Ação: "o-computador-nao-liga"

- **Requisitos:** "Computador-com-problema", "Computador-nao-liga"
- **Adiciona:** "checar-fonte"
- **Remove:** 

### Ação: "checar-se-a-fonte-inicia"

- **Requisitos:** "Computador-nao-liga", "checar-fonte"
- **Adiciona:** "fonte-inicia", "checar-voltagem"
- **Remove:** 

### Ação: "checar-se-voltagem-esta-correta"

- **Requisitos:** "Computador-com-problema", "Computador-nao-liga", "fonte-inicia", "checar-voltagem"
- **Adiciona:** "Voltagem-correta"
- **Remove:** "checar-voltagem"

### Ação: "checar-circuito-de-alimentacao"

- **Requisitos:** "Computador-com-problema", "Computador-nao-liga", "fonte-inicia", "Voltagem-correta"
- **Adiciona:** "circuito-de-alimentacao"
- **Remove:** 

### Ação: "Problema-no-circuito-de-alimentacao-da-placa-mae"

- **Requisitos:** "Computador-com-problema", "Computador-nao-liga", "fonte-inicia", "Voltagem-correta", "circuito-de-alimentacao"
- **Adiciona:** "Problema-detectado"
- **Remove:** "Computador-com-problema"

## Estado Final

- Problema detectado
