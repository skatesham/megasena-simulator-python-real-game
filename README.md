# Mega-Sena Simulator

Simulador em Python que reproduz jogos da Mega-Sena com apostas entre 6 e 15 dezenas. O programa mantém o mesmo conjunto sorteado até que um jogo aleatório acerte as seis dezenas, registrando estatísticas financeiras e temporais.

## Funcionalidades
- Escolha da quantidade de dezenas (6 a 15) com validação de entrada.
- Valores atualizados de cada tipo de aposta (segundo a tabela oficial de 2023).
- Sorteio único das dezenas vencedoras e geração de jogos aleatórios até acertar todas.
- Cálculo do gasto acumulado, número de tentativas e tempo "real" aguardando sorteios (assumindo calendário oficial de quartas e sábados).
- Exibição do tempo gasto pela simulação em segundos.

## Requisitos
- Python 3.8+

## Execução
```bash
python3 mega_sena_simulator.py
```

O script solicitará o número de dezenas desejadas e cuidará do restante.

## Exemplos de saída
```
=== Simulador de Jogos da Mega-Sena ===
Quantos números deseja jogar (6-15)? 14
...
Foram necessárias 7,132 tentativas
Gasto total: R$ 96,378,282.00
Tempo aguardando sorteios: 68 anos, 19 semanas e 5 dias
(Tempo de simulação: 0.05 segundos)
```
