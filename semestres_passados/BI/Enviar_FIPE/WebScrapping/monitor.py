import psutil
import time
import os

def monitor(pid):
    try:
        process = psutil.Process(pid)
        while True:
            # Uso de CPU em porcentagem
            cpu_usage = process.cpu_percent(interval=1)
            # Uso de memória em MB
            memory_usage = process.memory_info().rss / (1024 * 1024)
            os.system('clear')
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage} MB")
            
            # Pausa de 1 segundo antes de próxima medição
            time.sleep(1)
    except psutil.NoSuchProcess:
        print("Processo não encontrado")
    except KeyboardInterrupt:
        print("Monitoramento interrompido")

if __name__ == "__main__":
    # Substitua pelo PID do programa Python específico
    pid = int(input("Digite o PID do processo: "))
    monitor(pid)
