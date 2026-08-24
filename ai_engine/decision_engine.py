import psutil


def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    return cpu_usage, memory_usage


def calculate_risk(cpu, memory):
    risk = 0

    if cpu >= 80:
        risk += 50
    elif cpu >= 60:
        risk += 25

    if memory >= 80:
        risk += 50
    elif memory >= 60:
        risk += 25

    return min(risk, 100)


def make_decision(risk):
    if risk >= 75:
        return "HIGH RISK"
    elif risk >= 50:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


if __name__ == "__main__":

    cpu, memory = get_system_metrics()

    risk = calculate_risk(cpu, memory)

    decision = make_decision(risk)

    print("=================================")
    print(" AI PRE-DEPLOYMENT DECISION ENGINE")
    print("=================================")
    print(f"CPU Usage    : {cpu}%")
    print(f"Memory Usage : {memory}%")
    print(f"Risk Score   : {risk}/100")
    print(f"Decision     : {decision}")
    print("=================================")
