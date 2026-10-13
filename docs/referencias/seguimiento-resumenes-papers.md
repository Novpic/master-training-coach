# Seguimiento de resúmenes de papers

- **Creado:** 2026-10-09
- **Objetivo:** generar y auditar resúmenes técnicos con `paper-synthesizer` para los artículos con fuente extraída en `docs/referencias/papers-md/` y PDF asociado en `docs/referencias/papers-pdf/`.
- **Inventario:** 45 artículos en 9 lotes de 5.
- **Estado general:** Los 45 resúmenes están completos; todas las tandas restantes se ejecutaron.
- **Idioma:** inglés, según las instrucciones del agente `paper-synthesizer`.
- **Salida prevista:** `docs/referencias/papers-md-resume/<id>/<id>-resume.md`.
- **Regla de ejecución:** avanzar en lotes secuenciales de cinco, sin iniciar el siguiente hasta tener aprobación explícita del usuario.

## Procedimiento

1. Usar `papers-md/<id>/` como carpeta Marker de entrada y contrastar con `papers-pdf/<id>.pdf` cuando sea necesario.
2. Si falta el texto extraído o existe una discrepancia de identidad, no resumir solo desde metadatos o abstract: marcar `Bloqueado` y describir el motivo.
3. Crear el resumen en la carpeta de salida `papers-md-resume/<id>/`; conservar el PDF y los archivos originales de `papers-md/` sin cambios.
4. El resumen debe indicar la identidad y el tipo de documento/estudio, población y muestra (o aclarar si no aplica), métodos, comparador, resultados, limitaciones, alcance de aplicación y datos no verificados. No presentar ejemplos como protocolos universales ni convertir asociaciones en causalidad.
5. Anotar aquí el archivo de salida y el estado. Tras completar cada lote, detenerse y esperar autorización explícita antes de iniciar el siguiente.

## Estados

`Pendiente` · `En prueba` · `Revisión usuario` · `Completo` · `Bloqueado`

## Inventario por lotes

Rutas convencionales para cada artículo: fuente extraída `docs/referencias/papers-md/<id>/`, PDF `docs/referencias/papers-pdf/<id>.pdf`, salida `docs/referencias/papers-md-resume/<id>/<id>-resume.md`.

### Lote 1 (1–5)

| ID | Estado | Resumen |
|---|---|---|
| acsm2009progression | **Completo** | [acsm2009progression-resume.md](papers-md-resume/acsm2009progression/acsm2009progression-resume.md) |
| aragon2017diets | **Completo** | [aragon2017diets-resume.md](papers-md-resume/aragon2017diets/aragon2017diets-resume.md) — evidencia limitada en mujeres y adultos mayores; denominador no indicado para una afirmación general de >3 g/kg. |
| balsalobre2016economy | **Completo** | [balsalobre2016economy-resume.md](papers-md-resume/balsalobre2016economy/balsalobre2016economy-resume.md) — solo 5 ensayos, heterogeneidad y pequeñas discrepancias de estimación entre resumen y resultados. |
| bertelsen2017etiology | **Completo** | [bertelsen2017etiology-resume.md](papers-md-resume/bertelsen2017etiology/bertelsen2017etiology-resume.md) — marco conceptual, no predictor validado; carga/capacidad tisular difíciles de medir. |
| blagrove2018strength | **Completo** | [blagrove2018strength-resume.md](papers-md-resume/blagrove2018strength/blagrove2018strength-resume.md) — recuento inconsistente: total informado 469 frente a 448 al sumar el desglose por sexo. |

### Lote 2 (6–10)

| ID | Estado | Resumen |
|---|---|---|
| bosquet2007tapering | **Completo** | [bosquet2007tapering-resume.md](papers-md-resume/bosquet2007tapering/bosquet2007tapering-resume.md) — desajuste de identidad: el PDF y MD corresponden a Wang et al. (2023), no a Bosquet (2007); pocos estudios y heterogeneidad. |
| donnelly2009weightloss | **Completo** | [donnelly2009weightloss-resume.md](papers-md-resume/donnelly2009weightloss/donnelly2009weightloss-resume.md) — posicionamiento ACSM; evidencia débil para dosis de actividad física que evite la recuperación del peso perdido. |
| eddens2018sequence | **Completo** | [eddens2018sequence-resume.md](papers-md-resume/eddens2018sequence/eddens2018sequence-resume.md) — publicación en línea de 2017; 10 estudios, diseños y poblaciones heterogéneos. |
| fisher2017load | **Completo** | [fisher2017load-resume.md](papers-md-resume/fisher2017load/fisher2017load-resume.md) — el artículo es de opinión actual de 2016, no una revisión sistemática ni un ensayo. |
| gabbett2016paradox | **Completo** | [gabbett2016paradox-resume.md](papers-md-resume/gabbett2016paradox/gabbett2016paradox-resume.md) — evidencia principalmente observacional y de deportes de equipo; umbrales contextuales, algunos basados en datos no publicados. |

### Lote 3 (11–15)

| ID | Estado | Resumen |
|---|---|---|
| garber2011exercise | **Completo** | [garber2011exercise-resume.md](papers-md-resume/garber2011exercise/garber2011exercise-resume.md) — umbrales originales corregidos desde errores OCR; guía para adultos, evidencia consultada hasta 2010. |
| grgic2022failure | **Completo** | [grgic2022failure-resume.md](papers-md-resume/grgic2022failure/grgic2022failure-resume.md) — adultos jóvenes; solo dos estudios en subgrupo entrenado para hipertrofia. |
| guest2021caffeine | **Completo** | [guest2021caffeine-resume.md](papers-md-resume/guest2021caffeine/guest2021caffeine-resume.md) — evidencia heterogénea; respuesta individual, sueño y ansiedad son relevantes. |
| hewbutler2015hyponatremia | **Completo** | [hewbutler2015hyponatremia-resume.md](papers-md-resume/hewbutler2015hyponatremia/hewbutler2015hyponatremia-resume.md) — consenso experto; tratamiento requiere profesionales médicos cualificados. |
| jager2017protein | **Completo** | [jager2017protein-resume.md](papers-md-resume/jager2017protein/jager2017protein-resume.md) — parte de la evidencia es aguda (MPS); limitada evidencia longitudinal y de seguridad clínica. |

### Lote 4 (16–20)

| ID | Estado | Resumen |
|---|---|---|
| johnston2018enduranceinjury | **Completo** | [johnston2018enduranceinjury-resume.md](papers-md-resume/johnston2018enduranceinjury/johnston2018enduranceinjury-resume.md) — cohortes observacionales; definiciones y vigilancia de lesión heterogéneas. |
| jones2021sex | **Completo** | [jones2021sex-resume.md](papers-md-resume/jones2021sex/jones2021sex-resume.md) — calidad media moderada; asociaciones de programación exploratorias, no causales. |
| kassiano2023rom | **Completo** | [kassiano2023rom-resume.md](papers-md-resume/kassiano2023rom/kassiano2023rom-resume.md) — cita en línea 2022 frente a número/copyright 2023; estudios pequeños y mayormente cuádriceps. |
| kerksick2017timing | **Completo** | [kerksick2017timing-resume.md](papers-md-resume/kerksick2017timing/kerksick2017timing-resume.md) — posicionamiento contextual; evidencia limitada y mayormente masculina; diferencia interna en carbohidratos durante ejercicio. |
| kreider2017creatine | **Completo** | [kreider2017creatine-resume.md](papers-md-resume/kreider2017creatine/kreider2017creatine-resume.md) — posicionamiento amplio; declara relaciones con la industria y límites de inferencia clínica. |

### Lote 5 (21–25)

| ID | Estado | Resumen |
|---|---|---|
| lauersen2014prevention | **Completo** | [lauersen2014prevention-resume.md](papers-md-resume/lauersen2014prevention/lauersen2014prevention-resume.md) — heterogeneidad y efectos de estudios pequeños. |
| lundberg2022fiber | **Completo** | [lundberg2022fiber-resume.md](papers-md-resume/lundberg2022fiber/lundberg2022fiber-resume.md) — muestras pequeñas y variabilidad de biopsias musculares. |
| markov2022acute | **Completo** | [markov2022acute-resume.md](papers-md-resume/markov2022acute/markov2022acute-resume.md) — efectos agudos en hombres entrenados; subgrupos con pocos estudios. |
| maughan2018supplements | **Completo** | [maughan2018supplements-resume.md](papers-md-resume/maughan2018supplements/maughan2018supplements-resume.md) — consenso IOC; evidencia limitada en atletas de élite y riesgo de contaminación. |
| mikkonen2024femaleconcurrent | **Completo** | [mikkonen2024femaleconcurrent-resume.md](papers-md-resume/mikkonen2024femaleconcurrent/mikkonen2024femaleconcurrent-resume.md) — evidencia baja a moderada; no establece interferencia y duración inconsistente en el artículo. |

### Lote 6 (26–30)

| ID | Estado | Resumen |
|---|---|---|
| mountjoy2018reds | **Completo** | [mountjoy2018reds-resume.md](papers-md-resume/mountjoy2018reds/mountjoy2018reds-resume.md) — 30 kcal/kg FFM/día no es umbral diagnóstico universal; evidencia limitada en hombres y para-atletas. |
| mountjoy2023reds | **Completo** | [mountjoy2023reds-resume.md](papers-md-resume/mountjoy2023reds/mountjoy2023reds-resume.md) — consenso rechaza umbral único; CAT2 apoya evaluación, no sustituye diagnóstico médico. |
| morton2018protein | **Completo** | [morton2018protein-resume.md](papers-md-resume/morton2018protein/morton2018protein-resume.md) — punto de quiebre proteico no significativo; evidencia limitada en adultos mayores. |
| murphy2022energy | **Completo** | [murphy2022energy-resume.md](papers-md-resume/murphy2022energy/murphy2022energy-resume.md) — estimación de déficit derivada de cambio en grasa; LM del abstract −0.57 vs. cuerpo −0.58. |
| ralston2017volume | **Completo** | [ralston2017volume-resume.md](papers-md-resume/ralston2017volume/ralston2017volume-resume.md) — nueve estudios en hombres; categorías se solapan en cinco series semanales. |

### Lote 7 (31–35)

| ID | Estado | Resumen |
|---|---|---|
| ramirezcampillo2022spot | **Completo** | [ramirezcampillo2022spot-resume.md](papers-md-resume/ramirezcampillo2022spot/ramirezcampillo2022spot-resume.md) — definición estrecha de reducción localizada; reporte de eventos adversos incompleto. |
| ramoscampo2024split | **Completo** | [ramoscampo2024split-resume.md](papers-md-resume/ramoscampo2024split/ramoscampo2024split-resume.md) — abstract y resultados detallados informan estimaciones de masa magra en escalas distintas. |
| refalo2025sex | **Completo** | [refalo2025sex-resume.md](papers-md-resume/refalo2025sex/refalo2025sex-resume.md) — abstract y discusión difieren sobre hipertrofia absoluta del tren inferior. |
| rodriguez2009nutrition | **Completo** | [rodriguez2009nutrition-resume.md](papers-md-resume/rodriguez2009nutrition/rodriguez2009nutrition-resume.md) — posicionamiento histórico, en vigor hasta 2012; corregido error OCR en umbral de deshidratación. |
| robinson2024rir | **Completo** | [robinson2024rir-resume.md](papers-md-resume/robinson2024rir/robinson2024rir-resume.md) — meta-regresiones exploratorias, estimación RIR imprecisa y sin protocolo universal. |

### Lote 8 (36–40)

| ID | Estado | Resumen |
|---|---|---|
| sawka2007fluid | **Completo** | [sawka2007fluid-resume.md](papers-md-resume/sawka2007fluid/sawka2007fluid-resume.md) — hidratación individualizada y relevante para seguridad. |
| schoenfeld2016rest | **Completo** | [schoenfeld2016rest-resume.md](papers-md-resume/schoenfeld2016rest/schoenfeld2016rest-resume.md) — ensayo pequeño y breve en hombres jóvenes entrenados. |
| schoenfeld2017load | **Completo** | [schoenfeld2017load-resume.md](papers-md-resume/schoenfeld2017load/schoenfeld2017load-resume.md) — fallo muscular exigido en estudios; evidencia limitada en algunos resultados/poblaciones. |
| schoenfeld2017volume | **Completo** | [schoenfeld2017volume-resume.md](papers-md-resume/schoenfeld2017volume/schoenfeld2017volume-resume.md) — categorías de mayor volumen inciertas y sensibles a un estudio. |
| schoenfeld2019frequency | **Completo** | [schoenfeld2019frequency-resume.md](papers-md-resume/schoenfeld2019frequency/schoenfeld2019frequency-resume.md) — las conclusiones dependen de equiparar volumen; evidencia limitada para algunos grupos musculares. |

### Lote 9 (41–45)

| ID | Estado | Resumen |
|---|---|---|
| schumann2022compatibility | **Completo** | [schumann2022compatibility-resume.md](papers-md-resume/schumann2022compatibility/schumann2022compatibility-resume.md) — calidad modesta; separación de sesiones aplica al resultado de fuerza explosiva, no como regla universal. |
| singer2024rest | **Completo** | [singer2024rest-resume.md](papers-md-resume/singer2024rest/singer2024rest-resume.md) — nueve ensayos pequeños, cortos y heterogéneos; evidencia escasa en entrenados. |
| walsh2021sleep | **Completo** | [walsh2021sleep-resume.md](papers-md-resume/walsh2021sleep/walsh2021sleep-resume.md) — revisión/consenso narrativo centrado en atletas de élite; evidencia incompleta. |
| wewege2017hiit | **Completo** | [wewege2017hiit-resume.md](papers-md-resume/wewege2017hiit/wewege2017hiit-resume.md) — muestra y seguimiento pequeños; reporte de eventos adversos insuficiente. |
| wilson2012concurrent | **Completo** | [wilson2012concurrent-resume.md](papers-md-resume/wilson2012concurrent/wilson2012concurrent-resume.md) — 21 estudios heterogéneos; moderadores observacionales, no umbrales causales. |

## Registro de ejecuciones

- **Lotes 1–9 (artículos 1–45):** completados; todas las salidas están vinculadas por artículo. Los lotes 6 y 9 se reejecutaron tras quedar canceladas las llamadas anteriores; los archivos existentes se revisaron o actualizaron en el mismo destino, sin duplicados.
- **Verificación de fuentes:** los agentes comprobaron los Markdown Marker y los PDF correspondientes; los lotes 6 y 9 se releyeron y revisaron después de la reejecución.
- **Hallazgos de identidad:** los IDs `bosquet2007tapering` y `fisher2017load` no coinciden con los artículos realmente contenidos en los respectivos archivos; se conservaron los IDs para mantener el emparejamiento con los archivos fuente y se documentaron los nombres/años reales en los resúmenes. `eddens2018sequence` corresponde a un artículo publicado en línea en 2017.
- **Resultado:** no hubo artículos bloqueados; limitaciones, errores de extracción e inconsistencias bibliográficas se anotaron junto a las salidas pertinentes.
- **Estado final:** 45/45 resúmenes completos en nueve lotes de cinco.
