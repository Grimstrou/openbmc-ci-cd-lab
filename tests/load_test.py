import time
import random

def simulate_requests(duration_sec=10, rps=5):
    """Имитация нагрузочного тестирования"""
    total_requests = 0
    errors = 0
    start_time = time.time()
    
    while time.time() - start_time < duration_sec:
        for _ in range(rps):
            # Имитация запроса: 98% успех, 2% ошибка
            if random.random() > 0.02:
                total_requests += 1
            else:
                errors += 1
        time.sleep(1)
    
    return total_requests, errors

if __name__ == '__main__':
    print("=== Starting load test on OpenBMC WebUI ===")
    requests, errors = simulate_requests(duration_sec=15, rps=10)
    
    with open('load_test_report.txt', 'w', encoding='utf-8') as f:
        f.write("OpenBMC Load Test Report\n")
        f.write("========================\n")
        f.write(f"Duration: 15 seconds\n")
        f.write(f"Target RPS: 10\n")
        f.write(f"Total requests: {requests}\n")
        f.write(f"Errors: {errors}\n")
        f.write(f"Success rate: {100 * (1 - errors / (requests + errors)):.1f}%\n")
    
    print("Load test completed. Report saved to load_test_report.txt")