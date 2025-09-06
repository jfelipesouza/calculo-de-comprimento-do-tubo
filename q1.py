import sys
import math

if len(sys.argv) != 11:
    print("Uso: python3 q1.py D T_in T_out T_w v rho k cp mu Pr")
    print("----Unidades----")
    print("D (ft) - Diâmetro do tubo")
    print("T_in (°F) - Temperatura de entrada do fluido")
    print("T_out (°F) - Temperatura de saída do fluido")
    print("T_w (°F) - Temperatura da parede do tubo")
    print("v (ft/s) - Velocidade do fluido")
    print("rho (lb/ft^3) - Densidade do fluido")
    print("k (Btu/h.ft.°F) - Condutividade térmica do fluido")
    print("cp (Btu/lb.°F) - Calor específico do fluido")
    print("mu (lb/ft.s) - Viscosidade do fluido")
    print("Pr - Número de Prandtl")
    print("----------------")
    print("Exemplo: python3 q1.py 8.3e-3 60 100 150 1.6 54.6 0.092 0.42 3.96e-4 6.5")
    sys.exit(1)

try:
    D = float(sys.argv[1])
    T_in = float(sys.argv[2])
    T_out = float(sys.argv[3])
    T_w = float(sys.argv[4])
    v_ft_s = float(sys.argv[5])
    rho = float(sys.argv[6])
    k = float(sys.argv[7])
    cp = float(sys.argv[8])
    mu_ft_s = float(sys.argv[9])
    Pr = float(sys.argv[10])
except ValueError:
    print("Erro: Todos os parâmetros devem ser números.")
    sys.exit(1)


print("--- Parâmetros do Problema ---")
print(f"Diâmetro (D): {D} ft")
print(f"Temperatura de entrada (T_in): {T_in} °F")
print(f"Temperatura de saída (T_out): {T_out} °F")
print(f"Temperatura da parede (T_w): {T_w} °F")
print(f"Velocidade (v): {v_ft_s} ft/s")
print(f"Densidade (rho): {rho} lb/ft^3")
print(f"Condutividade térmica (k): {k} Btu/h.ft.°F")
print(f"Calor específico (cp): {cp} Btu/lb.°F")
print(f"Viscosidade (mu): {mu_ft_s} lb/ft.s")
print(f"Número de Prandtl (Pr): {Pr}")
print("-" * 30)


# --- Conversões de unidades (para consistência) ---
v_ft_h = v_ft_s * 3600
mu_ft_h = mu_ft_s * 3600

# --- Etapa 1: Calcular o número de Reynolds (Re) ---
Re = (rho * v_ft_h * D) / mu_ft_h
print(f"Número de Reynolds (Re): {Re:.2f}")

# --- Etapa 2: Calcular o Coeficiente de Transferência de Calor (h) ---
# Assumimos escoamento laminar totalmente desenvolvido, Nu = 3.66 (para Tw constante)
Nu = 3.66
h = (Nu * k) / D
print(f"Coeficiente de transferência de calor (h): {h:.2f} Btu/h.ft^2.°F")

# --- Etapa 3: Calcular a Média Logarítmica da Diferença de Temperatura (LMTD) ---
delta_T1 = T_w - T_in
delta_T2 = T_w - T_out

if delta_T1 == delta_T2:
    LMTD = delta_T1
else:
    LMTD = (delta_T1 - delta_T2) / math.log(delta_T1 / delta_T2)
print(f"Média logarítmica da diferença de temperatura (LMTD): {LMTD:.2f} °F")

# --- Etapa 4: Calcular a Taxa de Transferência de Calor (Q) ---
A = (math.pi * D**2) / 4
m_dot_lb_s = rho * A * v_ft_s
m_dot_lb_h = m_dot_lb_s * 3600
print(f"Vazão mássica (m_dot): {m_dot_lb_h:.2f} lb/h")
Q = m_dot_lb_h * cp * (T_out - T_in)
print(f"Taxa de transferência de calor (Q): {Q:.2f} Btu/h")

# --- Etapa 5: Calcular o Comprimento do Tubo (L) ---
L = Q / (h * math.pi * D * LMTD)
print(f"Comprimento do tubo necessário (L): {L:.4f} ft")