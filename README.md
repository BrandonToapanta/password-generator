# 🔐 Generador Seguro de Contraseñas (Arquitectura MVC)

## 📖 Descripción

Este proyecto consiste en un **Generador Seguro de Contraseñas** desarrollado en **Python**, implementado bajo el patrón de arquitectura **Model-View-Controller (MVC)**. Su objetivo es generar contraseñas robustas utilizando mecanismos criptográficos seguros y validar automáticamente su cumplimiento con políticas de seguridad definidas.

A diferencia de los generadores convencionales basados en algoritmos pseudoaleatorios, este sistema emplea un **Generador de Números Aleatorios Criptográficamente Seguro (CSPRNG)** mediante el módulo nativo `secrets` de Python, reduciendo significativamente la posibilidad de predicción de las contraseñas generadas.

Además, incorpora cálculos matemáticos de entropía, validaciones de complejidad y filtros configurables para mejorar tanto la seguridad como la usabilidad.

---

# ✨ Características Principales

### 🔒 Generación Criptográficamente Segura

Utiliza el módulo `secrets` de Python para generar contraseñas mediante un CSPRNG (Cryptographically Secure Pseudo-Random Number Generator), garantizando un nivel de aleatoriedad adecuado para aplicaciones de seguridad.

### ✅ Cumplimiento Obligatorio de Categorías

Asegura que la contraseña incluya al menos un carácter de cada categoría seleccionada:

* Letras mayúsculas (`A-Z`)
* Letras minúsculas (`a-z`)
* Números (`0-9`)
* Símbolos especiales (`!@#$%^&*`, etc.)

### 👁️ Filtro de Caracteres Ambiguos

Permite excluir caracteres visualmente similares para evitar errores de lectura o transcripción:

| Caracteres Ambiguos |   |
| ------------------- | - |
| O, 0                |   |
| l, 1                |   |
| I,                  |   |

### 📊 Cálculo de Entropía

Calcula la fortaleza teórica de la contraseña utilizando la fórmula:

```text
E = L × log₂(N)
```

Donde:

* **E** = Entropía en bits
* **L** = Longitud de la contraseña
* **N** = Tamaño del conjunto de caracteres utilizado

### 🛡️ Validación de Políticas de Seguridad

Verifica automáticamente:

* Longitud mínima requerida
* Presencia de mayúsculas
* Presencia de minúsculas
* Presencia de números
* Presencia de símbolos
* Entropía mínima configurable
* Ausencia de patrones inseguros comunes

---

# 📂 Estructura del Proyecto

El sistema implementa el patrón **MVC (Model-View-Controller)** con el objetivo de mantener una clara separación de responsabilidades.

```text
password-generator/
│
├── docs/                           # Diagramas funcionales y arquitectónicos
│   ├── diagrama_caso_uso.png
│   └── diagrama_flujo.png
│   └── diagrama_uml.png
│
├── src/                            # Código fuente de la aplicación
│   ├── __init__.py
│   │
│   ├── model/                      # Lógica de negocio y estructuras de datos
│   │   ├── __init__.py
│   │   ├── password_options.py     # DTO de configuraciones del usuario
│   │   ├── password_policy.py      # Umbrales y reglas de seguridad
│   │   ├── character_set.py        # Composición de alfabetos y CSPRNG
│   │   └── validation_result.py    # DTO del estado de validación
│   │
│   ├── controller/                 # Orquestador del flujo lógico
│   │   ├── __init__.py
│   │   └── password_controller.py  # Generador, Validador y Calculador
│   │
│   └── view/                       # Interfaz de usuario (Consola)
│       ├── __init__.py
│       └── cli_view.py             # Captura de datos y renderizado visual
│
├── main.py                         # Punto de entrada de la aplicación
├── README.md                       # Documentación del proyecto
└── .gitignore                      # Exclusiones de Git
```

---

# ⚙️ Requisitos

## Software requerido

* Python 3.11 o superior
* Git

Verificar la versión instalada:

```bash
python --version
```

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/BrandonToapanta/password-generator.git
```

## 2. Ingresar al proyecto

```bash
cd password-generator
```

## 3. Ejecutar la aplicación

```bash
python main.py
```

---

# 💻 Ejemplo de Uso

## Caso Exitoso

```text
--- CONFIGURACIÓN DEL GENERADOR SEGURO ---

Ingrese longitud de la contraseña: 16
¿Incluir mayúsculas? (s/n): s
¿Incluir minúsculas? (s/n): s
¿Incluir números? (s/n): s
¿Incluir símbolos? (s/n): s
¿Incluir caracteres ambiguos (O, 0, l, 1)? (s/n): n

--- RESULTADO DE GENERACIÓN ---

Contraseña Generada: k#P9x$m2_Wv!Rt4Z
Entropía Matemática: 90.22 bits

Estado de la política:
¡CUMPLE CON TODAS LAS REGLAS DE SEGURIDAD!
```

---

## Caso Rechazado por la Política

```text
--- CONFIGURACIÓN DEL GENERADOR SEGURO ---

Ingrese longitud de la contraseña: 6
¿Incluir mayúsculas? (s/n): s
¿Incluir minúsculas? (s/n): s
¿Incluir números? (s/n): n
¿Incluir símbolos? (s/n): n
¿Incluir caracteres ambiguos (O, 0, l, 1)? (s/n): n

--- RESULTADO DE GENERACIÓN ---

Contraseña Generada: aBxFgT
Entropía Matemática: 34.20 bits

Estado de la política:
RECHAZADA POR LA POLÍTICA

- Error: La longitud es menor a 12 caracteres.
- Error: Faltan dígitos numéricos.
- Error: Faltan caracteres especiales o símbolos.
- Error: Entropía insuficiente (34.20 bits).
  Mínimo requerido: 60.00 bits.
```

---

# 📐 Fundamento Matemático

La seguridad de una contraseña puede estimarse mediante su entropía:

```text
E = L × log₂(N)
```

### Ejemplo

Contraseña de 16 caracteres utilizando un conjunto de 50 símbolos:

```text
E = 16 × log₂(50)

E ≈ 90.22 bits
```

Cuanto mayor sea la entropía, mayor será la resistencia frente a ataques de fuerza bruta.

---

# 🔐 Consideraciones de Seguridad

* Uso exclusivo de generadores criptográficamente seguros (`secrets`).
* Inclusión obligatoria de categorías seleccionadas.
* Eliminación opcional de caracteres ambiguos.
* Validación de políticas configurables.
* Cálculo matemático de fortaleza basado en entropía.
* Arquitectura desacoplada para facilitar mantenimiento y auditoría.

---

# 👨‍💻 Autor

**Brandon Ramiro Toapanta Basantes**

Desarrollador de Software especializado en desarrollo web, backend y soluciones empresariales utilizando tecnologías modernas y buenas prácticas de ingeniería de software.