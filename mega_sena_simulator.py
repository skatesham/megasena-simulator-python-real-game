import random
import time
from datetime import timedelta

def generate_ticket(numbers_to_play):
    """Generate a sorted list of unique random numbers between 1 and 60."""
    return sorted(random.sample(range(1, 61), numbers_to_play))

def generate_draw():
    """Generate the winning numbers (6 numbers)."""
    return sorted(random.sample(range(1, 61), 6))

def check_win(ticket, draw):
    """Check how many numbers match between ticket and draw."""
    return len(set(ticket) & set(draw))

def get_ticket_cost(numbers_played):
    """Return the cost of a ticket based on the number of numbers played."""
    # Prices in BRL as of 2023
    prices = {
        6: 4.50,
        7: 31.50,
        8: 126.00,
        9: 378.00,
        10: 945.00,
        11: 2079.00,
        12: 4158.00,
        13: 7722.00,
        14: 13513.50,
        15: 22522.50
    }
    return prices.get(numbers_played, 0)

def compute_elapsed_time(draws_played):
    """Return timedelta representing real-world time waiting for draws (Wed/Sat schedule)."""
    if draws_played <= 1:
        return timedelta(0)
    intervals = [3, 4]  # days between Wednesday→Saturday and Saturday→Wednesday draws
    total_days = 0
    for i in range(draws_played - 1):
        total_days += intervals[i % len(intervals)]
    return timedelta(days=total_days)

def main():
    print("=== Simulador de Jogos da Mega-Sena ===\n")
    
    # Get valid input for number of numbers to play
    while True:
        try:
            numbers_to_play = int(input("Quantos números deseja jogar (6-15)? "))
            if 6 <= numbers_to_play <= 15:
                break
            print("Por favor, escolha um número entre 6 e 15.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    ticket_cost = get_ticket_cost(numbers_to_play)
    if ticket_cost == 0:
        print("Erro: Número de dezenas inválido.")
        return
    
    print(f"\nCada jogo de {numbers_to_play} números custa R$ {ticket_cost:.2f}")
    print(f"Gerando jogos até acertar os 6 números sorteados...\n")
    
    start_time = time.time()
    attempts = 0
    total_spent = 0.0
    
    # Generate the winning numbers
    winning_numbers = generate_draw()
    print(f"Números sorteados: {', '.join(map(str, winning_numbers))}\n")
    
    try:
        while True:
            attempts += 1
            total_spent += ticket_cost
            
            # Generate a ticket and check for matches
            my_numbers = generate_ticket(numbers_to_play)
            matches = check_win(my_numbers, winning_numbers)
            
            # Print progress every 1,000,000 attempts
            if attempts % 1000000 == 0:
                print(f"Tentativa: {attempts:,} | Gasto total: R$ {total_spent:,.2f}")
            
            # Check for win
            if matches == 6:
                sim_runtime = time.time() - start_time
                elapsed_wait = compute_elapsed_time(attempts)
                total_days = elapsed_wait.days
                years, remaining_days = divmod(total_days, 365)
                weeks, days = divmod(remaining_days, 7)
                
                print("\n" + "="*50)
                print("PARABÉNS! Você ganhou na Mega-Sena!")
                print(f"Números sorteados: {', '.join(map(str, winning_numbers))}")
                print(f"Seu jogo: {', '.join(map(str, my_numbers))}")
                print(f"\nForam necessárias {attempts:,} tentativas")
                print(f"Gasto total: R$ {total_spent:,.2f}")
                print(f"Tempo aguardando sorteios: {years} anos, {weeks} semanas e {days} dias")
                print(f"(Tempo de simulação: {sim_runtime:.2f} segundos)")
                print("="*50)
                break
                
    except KeyboardInterrupt:
        sim_runtime = time.time() - start_time
        elapsed_wait = compute_elapsed_time(attempts)
        print("\n\nSimulação interrompida pelo usuário.")
        print(f"Tentativas: {attempts:,}")
        print(f"Gasto total: R$ {total_spent:,.2f}")
        print(f"Tempo aguardando sorteios (simulado): {elapsed_wait.days} dias")
        print(f"(Tempo de simulação: {sim_runtime:.2f} segundos)")

if __name__ == "__main__":
    main()
