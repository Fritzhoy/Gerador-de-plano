## LISTA DE REGRAS

### REGRA 1

SE (o computador liga                  = Sim)
E (A BIOS está iniciando     = Sim)
E (O Sistema Operacional inicia    = Sim)
E (O sistema operacional inicia completamente  = Sim)
ENTÃO (Sem problemas, tudo normal)

### REGRA 2

SE (o computador liga                  = Sim)
E (A BIOS está iniciando     = Sim)
E (O Sistema Operacional inicia    = Sim)
E (O sistema operacional inicia completamente  = Não)
ENTÃO (O Sistema Operacional está corrompido)

### REGRA 3

SE (o computador liga                 = Sim)
E (A BIOS está iniciando     = Sim) 
E (O Sistema Operacional inicia    = Não)
E (A unidade de armazenamento é detectada               = Sim)
E (A ordem de boot está correta                = Sim)
E (A unidade de armazenamento está íntegra               = Sim)
ENTÃO (O Sistema Operacional está corrompido)

### REGRA 4

SE (o computador liga      = Sim)
E (A BIOS está iniciando     = Sim) 
E (O Sistema Operacional inicia    = Não)
E (A unidade de armazenamento é detectada               = Sim)
E (A ordem de boot está correta                = Sim)
E (A unidade de armazenamento está íntegra               = Não)
ENTÃO (Troque o HD/SDD)

### REGRA 5

SE (o computador liga     = Sim)
E (A BIOS está iniciando    = Sim) 
E (O Sistema Operacional inicia   = Não)
E (A unidade de armazenamento é detectada  = Sim)
E (A ordem de boot está correta   = Não)
ENTÃO (Ajustar Boot)

### REGRA 6

SE (o computador liga      = Sim)
E (A BIOS está iniciando     = Sim) 
E (O Sistema Operacional inicia    = Não)
E (A unidade de armazenamento é detectada   = Não)
ENTÃO (HD está desconectado ou com problema)

### REGRA 7

SE (o computador liga      = Sim)
E (A BIOS está iniciando     = Não)
E (O speaker emite alertas     = Sim)
ENTÃO (Problema na memória ou processador)

### REGRA 8

SE (o computador liga    = Sim)
E (A BIOS está iniciando   = Não)
E (O speaker emite alertas   = Não)
ENTÃO (Problema na placa mãe)

### REGRA 9

SE (o computador não liga   = Não)
E (A fonte inicia     = Sim)
E (A voltagem está correta    = Sim)
ENTÃO (Problema no circuito da Placa Mãe)

### REGRA 10

SE (o computador não liga   = Não)
E (A fonte inicia    = Sim)
E (A voltagem está correta   = Não)
ENTÃO (A fonte está com problema)

### REGRA 11

SE (o computador não liga   = Não)
E (A fonte inicia    = Não)
E (A alimentacao está conectada  = Sim)
ENTÃO (A fonte está queimada)

### REGRA 12

SE (o computador não liga   = Não)
E (A fonte inicia    = Não)
E (A alimentacao está conectada  = Não)
ENTÃO (Ligar na tomada)
