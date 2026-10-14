# Plan de entrenamiento basado en evidencia

Repositorio documental para investigar y organizar conocimiento sobre fuerza,
carrera, hipertrofia, nutricion deportiva y recuperacion.

## Proposito

El repositorio separa la evidencia general de los planes personales. La
documentacion publica sirve como base educativa y debe mantener trazabilidad de
fuentes, limites de aplicabilidad y estado de acceso. Los planes individualizados,
fotografias, mediciones y datos personales permanecen fuera de Git.

## Estructura

```text
.
├── README.md                 # Mapa general y reglas de trabajo
├── AGENTS.md                 # Instrucciones operativas del repositorio
├── docs/                     # Documentacion educativa versionable
│   ├── README.md             # Indice y alcance de la coleccion
│   ├── metodologia/          # Como investigar, redactar y auditar
│   ├── bibliografia.md       # Indice tematico de referencias
│   ├── referencia.bib        # Bibliografia normalizada
│   └── *.md                  # Temas educativos publicados
├── .agent/                   # Roles y criterios de investigacion
├── .agents/                  # Instrucciones portables y generador de adapters
│   └── skills/               # Agent Skills compartibles entre harnesses
├── .coach-kit/               # Contrato y soporte de coaches, reutilizable por cualquier harness
├── .opencode/                # Adaptadores de agentes y skills locales
│   └── agents/               # Solo definiciones de agentes (orquestador, 7 coaches, investigacion)
├── .claude/                  # Adaptadores de subagentes para Claude Code
│   └── agents/               # Definiciones de subagentes del proyecto
├── .codex/                   # Adaptadores de subagentes para Codex
│   └── agents/               # Definiciones TOML del proyecto
├── datos/                    # Perfiles privados datos-<nombre>.md, ignorado por Git
├── planes/                   # Planes generados, privado, ignorado por Git
└── docs/fotos/               # Privado, ignorado por Git
```

Las carpetas `planes/`, `docs/fotos/` y `docs/forots/` estan excluidas mediante
variante del nombre; la carpeta existente actualmente es `docs/fotos/`.

## Como trabajar

1. Define antes de investigar la pregunta, poblacion, intervencion o exposicion,
   comparador, resultados, duracion y exclusiones.
2. Lee `AGENTS.md`, la metodologia aplicable y la auditoria mas reciente.
3. Usa `docs/metodologia/plantilla-investigacion.md` para investigaciones nuevas.
4. Prioriza revisiones sistematicas, metaanalisis, consensos, guias y estudios
   primarios relevantes. Verifica los identificadores en una fuente independiente.
5. Separa siempre resultado de la fuente, interpretacion y aplicacion practica.
6. Añade las citas junto a las afirmaciones materiales y sincroniza
   `docs/bibliografia.md` con `docs/referencia.bib`.
7. Revisa enlaces, identificadores, contradicciones, acceso legal y extrapolaciones
   antes de publicar cambios.
8. Solicita reauditoria cuando una modificacion cambie recomendaciones, cifras,
   seguridad o el alcance de una conclusion.

## Agentes para planes de entrenamiento

La forma recomendada es seleccionar `training-plan-orchestrator` con Tab (agente
primario) o invocarlo con `@training-plan-orchestrator`. Pide en una sola ronda solo
los datos que faltan en el perfil, ejecuta los coaches en orden de dependencia y
combina sus resultados en un plan maestro.

| Agente | Para que sirve |
| --- | --- |
| `@gym-coach` | Plan general de fuerza: una tabla por dia, ejercicios principales, core y progresion. |
| `@hypertrophy-coach` | Plan de hipertrofia nuevo o refinamiento de un plan de `gym-coach`. |
| `@running-coach` | Plan de carrera o carrera/caminata alrededor del horario de fuerza. |
| `@concurrent-training-coach` | Organiza en la semana las sesiones ya escritas; no cambia prescripciones. |
| `@sports-nutrition-coach` | Estrategia nutricional, menus por dia, lista de compras y sustituciones economicas. |
| `@recovery-health-coach` | Revision de recuperacion y seguridad; tambien va primero si hay un sintoma. |
| `@fat-loss-coach` | Implementacion de perdida de grasa usando los planes ya completos; siempre va al final. |

Todos siguen el contrato comun `.coach-kit/protocol.md`:

- Leen el perfil `datos/datos-<nombre>.md` antes de preguntar y guardan ahi los
  datos nuevos reportados por la persona, con fecha.
- Responden con un encabezado, una tabla por dia con columnas fijas y un bloque
  `Handoff` final con uno de cinco estados: `COMPLETE`, `NEEDS_INPUT`,
  `PAUSED_SAFETY`, `BLOCKED_DEPENDENCY` o `NEEDS_REVISION`.
- Guardan cada resultado en `planes/<nombre>/<dominio>/<AAAA-MM-DD>.md`; el
  orquestador los combina en `planes/<nombre>/master-plan/<AAAA-MM-DD>.md`.
- No incluyen citas ni referencias en sus respuestas: la evidencia de
  `.coach-kit/` es solo de uso interno.

Las dependencias se ejecutan en secuencia (por ejemplo, `gym-coach` antes de
`hypertrophy-coach`, y `fat-loss-coach` siempre al final). Una pausa de seguridad
detiene toda la cadena. `opencode.json` define `experimental.subagent_depth: 2`
para que el orquestador tambien pueda delegar cuando se invoca con `@`; reinicia
OpenCode despues de modificar agentes o configuracion.

## Uso de planes personales

Los planes individuales pueden mantenerse localmente bajo `planes/`, pero no deben
subirse al repositorio ni incluirse en commits. Los perfiles personales de `datos/`
tambien quedan excluidos. Para compartir una
plantilla, anonimiza nombres, medidas, fotografias, fechas identificables y
cualquier dato de salud; coloca solo la plantilla general en `docs/` o `datos/`.

Antes de cada commit comprueba las exclusiones:

```bash
git status --short --ignored
git check-ignore -v planes/ datos/ docs/fotos/ docs/forots/
```

## Estado de la evidencia

La documentacion es educativa y no sustituye una evaluacion medica. No se hacen
recomendaciones clinicas individualizadas. Las afirmaciones no confirmadas deben
marcarse como `No verificado`, y el acceso a un registro bibliografico no debe
confundirse con acceso al texto completo.
