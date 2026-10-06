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
├── .opencode/                # Agentes y skills locales
├── datos/                    # Datos anonimizados o plantillas no sensibles
├── planes/                   # Privado, ignorado por Git
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

## Uso de planes personales

Los planes individuales pueden mantenerse localmente bajo `planes/`, pero no deben
subirse al repositorio ni incluirse en commits. Los archivos personales con el
patron `datos/datos-camilo.*` tambien quedan excluidos. Para compartir una
plantilla, anonimiza nombres, medidas, fotografias, fechas identificables y
cualquier dato de salud; coloca solo la plantilla general en `docs/` o `datos/`.

Antes de cada commit comprueba las exclusiones:

```bash
git status --short --ignored
git check-ignore -v planes/ docs/fotos/ docs/forots/
```

## Estado de la evidencia

La documentacion es educativa y no sustituye una evaluacion medica. No se hacen
recomendaciones clinicas individualizadas. Las afirmaciones no confirmadas deben
marcarse como `No verificado`, y el acceso a un registro bibliografico no debe
confundirse con acceso al texto completo.
