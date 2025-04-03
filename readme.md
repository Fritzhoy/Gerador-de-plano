## Estado Inicial

- Caso 1: "Computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-emite-alerta"

## Caso 1

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

- Caso 2: "Computador-com-problema", "Computador-nao-liga"
- Caso 3: "Computador-com-problema", "checar-computador-liga", "a-bios-nao-inicia", "Speaker-nao-emite-alerta"

## Estado Final

- Problema detectado
