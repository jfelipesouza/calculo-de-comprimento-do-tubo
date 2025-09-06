const D = 8.3e-3 // ft
const T_in = 60 // °F
const T_out = 100 // °F
const T_w = 150 // °F
const v_ft_s = 1.6 // ft/s
const rho = 54.6 // lb/ft^3
const k = 0.092 // Btu/h.ft.°F
const cp = 0.42 // Btu/lb.°F
const mu_ft_s = 3.96e-4 // lb/ft.s
const Pr = 6.5 // adimensional

console.log('--- Parâmetros do Problema ---')
console.log(`Diâmetro (D): ${D} ft`)
console.log(`Temperatura de entrada (T_in): ${T_in} °F`)
console.log(`Temperatura de saída (T_out): ${T_out} °F`)
console.log(`Temperatura da parede (T_w): ${T_w} °F`)
console.log(`Velocidade (v): ${v_ft_s} ft/s`)
console.log(`Densidade (rho): ${rho} lb/ft^3`)
console.log(`Condutividade térmica (k): ${k} Btu/h.ft.°F`)
console.log(`Calor específico (cp): ${cp} Btu/lb.°F`)
console.log(`Viscosidade (mu): ${mu_ft_s} lb/ft.s`)
console.log(`Número de Prandtl (Pr): ${Pr}`)
console.log('-'.repeat(30))

// Conversões
const v_ft_h = v_ft_s * 3600
const mu_ft_h = mu_ft_s * 3600

// Reynolds
const Re = (rho * v_ft_h * D) / mu_ft_h
console.log(`Número de Reynolds (Re): ${Re.toFixed(2)}`)

// Coef. de transferência de calor
const Nu = 3.66
const h = (Nu * k) / D
console.log(
  `Coeficiente de transferência de calor (h): ${h.toFixed(2)} Btu/h.ft^2.°F`
)

// LMTD
const delta_T1 = T_w - T_in
const delta_T2 = T_w - T_out
let LMTD
if (delta_T1 === delta_T2) {
  LMTD = delta_T1
} else {
  LMTD = (delta_T1 - delta_T2) / Math.log(delta_T1 / delta_T2)
}
console.log(
  `Média logarítmica da diferença de temperatura (LMTD): ${LMTD.toFixed(2)} °F`
)

// Vazão mássica
const A = (Math.PI * D ** 2) / 4
const m_dot_lb_s = rho * A * v_ft_s
const m_dot_lb_h = m_dot_lb_s * 3600
console.log(`Vazão mássica (m_dot): ${m_dot_lb_h.toFixed(2)} lb/h`)

// Taxa de calor
const Q = m_dot_lb_h * cp * (T_out - T_in)
console.log(`Taxa de transferência de calor (Q): ${Q.toFixed(2)} Btu/h`)

// Comprimento do tubo
const L = Q / (h * Math.PI * D * LMTD)
console.log(`Comprimento do tubo necessário (L): ${L.toFixed(4)} ft`)
