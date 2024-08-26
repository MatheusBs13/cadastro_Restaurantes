import time
import psutil
from fpdf import FPDF

# Função para monitorar a CPU e a RAM


def monitor_system(duration=10, interval=1):
    cpu_usage = []
    ram_usage = []

    for _ in range(int(duration / interval)):
        cpu = psutil.cpu_percent(interval=interval)
        ram = psutil.virtual_memory().percent
        cpu_usage.append(cpu)
        ram_usage.append(ram)
        print(f"CPU: {cpu}% | RAM: {ram}%")

    return cpu_usage, ram_usage

# Função para gerar o PDF


def generate_pdf(cpu_usage, ram_usage, filename="system_monitoring_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="System Monitoring Report", ln=True, align="C")

    pdf.ln(10)
    pdf.cell(200, 10, txt="CPU and RAM Usage Over Time", ln=True, align="L")

    pdf.ln(5)
    for i, (cpu, ram) in enumerate(zip(cpu_usage, ram_usage)):
        pdf.cell(200, 10, txt=f"Second {
                 i+1}: CPU: {cpu}% | RAM: {ram}%", ln=True, align="L")

    pdf.output(filename)


if __name__ == "__main__":
    duration = 10  # Duração do monitoramento em segundos
    interval = 1  # Intervalo de medição em segundos

    cpu_usage, ram_usage = monitor_system(duration=duration, interval=interval)
    generate_pdf(cpu_usage, ram_usage)
