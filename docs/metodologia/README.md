# Metodologia para investigar temas nuevos

Esta guia define como incorporar un tema nuevo a la documentacion deportiva del proyecto. El objetivo es producir contenido exacto, trazable, actualizado y prudente para adultos sanos y poblaciones recreativas, sin convertir resultados cientificos en prescripciones universales.

## Principios obligatorios

- Definir primero la pregunta y la poblacion; no empezar por una recomendacion.
- Separar tres niveles: resultado de la fuente, interpretacion y aplicacion practica.
- Priorizar fuentes primarias, revisiones sistematicas, metaanalisis, consensos y organismos oficiales.
- Confirmar la identidad de cada fuente con DOI, PMID, editorial o registro institucional.
- No usar blogs, redes sociales, Wikipedia, snippets de buscador ni contenido generado por IA como evidencia final.
- No presentar un DOI o PubMed como prueba de acceso abierto.
- Si un dato no puede verificarse, escribir `No verificado` o reformularlo como pendiente.
- No convertir una heuristica, un ejemplo o una practica habitual en una ley universal.
- Mantener las recomendaciones proporcionales a la fuerza y aplicabilidad de la evidencia.
- Toda afirmacion material debe poder rastrearse desde el texto hasta una fuente concreta.

## Flujo recomendado

### 1. Definir el alcance

Antes de buscar, registrar:

- Tema y nombre provisional del documento.
- Pregunta principal que se quiere responder.
- Poblacion: edad, sexo, nivel de entrenamiento y estado de salud.
- Intervencion o exposicion.
- Comparador.
- Resultados relevantes.
- Contexto: modalidad, duracion, frecuencia y objetivo.
- Decisiones practicas que el lector podria tomar.
- Exclusiones: lesiones, enfermedades, embarazo u otras poblaciones que no se cubriran.

Una pregunta vaga como "que funciona mejor" debe convertirse en una pregunta concreta, por ejemplo: "En adultos sanos recreativamente activos, ¿como afecta entrenar fuerza dos veces por semana frente a una vez al volumen muscular durante al menos ocho semanas?".

### 2. Crear un inventario de afirmaciones

Separar el borrador en afirmaciones pequenas. Para cada una identificar:

- Poblacion.
- Intervencion o exposicion.
- Comparador.
- Resultado.
- Magnitud, rango, dosis o duracion.
- Condiciones y limitaciones.
- Recomendacion practica derivada.

Marcar especialmente numeros, porcentajes, dosis, umbrales, afirmaciones causales, recomendaciones de salud y frases como "siempre", "nunca", "la mayoria" o "optimo".

### 3. Buscar la evidencia

Usar este orden inicial:

1. Revisiones sistematicas y metaanalisis recientes para preguntas generales.
2. Consensos, guias y documentos de posicion de sociedades profesionales u organismos oficiales.
3. Estudios primarios para dosis, poblaciones, protocolos, resultados concretos o discrepancias.
4. Registros bibliograficos de PubMed, Crossref, Europe PMC y editoriales para confirmar identidad.

La fecha de publicacion no basta para elegir una fuente. Comprobar si existen actualizaciones, correcciones, retractaciones o consensos posteriores.

### 4. Comprobar cada fuente

Para cada fuente registrar:

- Autores y titulo completo.
- Revista u organismo.
- Año, volumen, numero y paginas.
- DOI, PMID, PMCID o identificador oficial.
- Tipo de evidencia y jerarquia.
- Poblacion y tamaño de muestra.
- Intervencion, comparador y duracion.
- Resultado principal y magnitud del efecto, si existe.
- Limitaciones, sesgos y conflictos de interes.
- URL legal.
- Estado de acceso: registro accesible, texto completo accesible, descarga verificable, acceso restringido, enlace roto o no comprobable.
- Fecha de comprobacion.

Nunca afirmar que un PDF fue descargado o analizado si no se comprobó. No incorporar copias no autorizadas al repositorio.

### 5. Evaluar la fuerza de la evidencia

Clasificar la relacion entre fuente y afirmacion:

- **Directa:** estudia la poblacion, intervencion, comparador y resultado relevantes.
- **Indirecta:** trata un contexto parecido, pero requiere extrapolacion.
- **Contradictoria:** fuentes razonables llegan a resultados diferentes.
- **Ausente:** no se encontro una fuente suficiente.

Usar estos veredictos:

- **Verificada:** la fuente es localizable, respalda la afirmacion y el alcance esta delimitado.
- **Parcialmente verificada:** existe respaldo, pero faltan matices o la redaccion es mas fuerte.
- **No verificada:** no se pudo confirmar la fuente o la afirmacion concreta.
- **Incorrecta:** la evidencia contradice la afirmacion o existe un error factual.

### 6. Redactar sin sobreafirmar

Cada bloque importante debería seguir esta secuencia:

1. **Lo que muestra la evidencia:** resultado concreto y poblacion estudiada.
2. **Lo que no demuestra:** limites, incertidumbre y poblaciones no estudiadas.
3. **Aplicacion practica:** opcion prudente y ajustable, no receta universal.
4. **Condiciones para cambiarla:** rendimiento, sintomas, recuperacion, objetivo o contexto.

Ejemplo:

> En estudios de adultos entrenados, una mayor frecuencia no siempre mejora la hipertrofia cuando el volumen semanal es equivalente. En principiantes y otros objetivos la aplicabilidad es incierta. Por eso, repartir el volumen en dos sesiones puede ser un punto de partida practico si mejora la calidad, pero no es una dosis obligatoria.

### 7. Editar el documento

- Añadir citas inline junto a afirmaciones materiales.
- Mantener una lista final de referencias con metadatos suficientes.
- Usar lenguaje condicional cuando la evidencia sea indirecta.
- Etiquetar ejemplos, rangos orientativos y heuristicas como tales.
- Añadir advertencias para dolor, enfermedad, embarazo, medicacion o baja disponibilidad energetica cuando corresponda.
- No añadir recomendaciones clinicas individualizadas ni promesas de rendimiento.
- Actualizar `docs/bibliografia.md` y `docs/referencia.bib` sin borrar entradas validas no relacionadas.
- Revisar enlaces internos y evitar contradicciones con otros documentos.

### 8. Hacer la revisión humana

La revisión humana es obligatoria cuando el tema incluye:

- Dolor, lesiones, sintomas, diagnóstico o retorno al deporte.
- Embarazo, enfermedad, medicación o suplementos.
- Umbrales de seguridad o criterios de derivación.
- Recomendaciones específicas para principiantes.
- Productos comerciales, contaminación o certificaciones.
- Fuentes cuyo texto completo o estado de acceso no pudo comprobarse.

La persona revisora debe confirmar la aplicabilidad al lector previsto, detectar lenguaje clínico excesivo y decidir si una recomendación debe conservarse, rebajarse o eliminarse.

### 9. Reauditar antes de publicar

Comprobar:

- Cada afirmacion material tiene fuente o está marcada como pendiente.
- DOI, PMID, título, autores y páginas coinciden.
- No hay PMID o DOI de otro artículo.
- No hay enlaces rotos ni acceso abierto declarado sin prueba.
- Las cifras tienen población, contexto y unidad.
- Los ejemplos no parecen protocolos universales.
- Las fuentes contradictorias están descritas.
- `bibliografia.md` y `referencia.bib` están sincronizados.
- El documento no contradice otros documentos del proyecto.
- Se registran hallazgos resueltos, parciales y pendientes.

## Roles de agentes

### Verificador de verdad deportiva

Audita sin editar. Extrae afirmaciones, verifica fuentes, identifica desajustes y entrega hallazgos ordenados por severidad.

### Investigador-ejecutor de evidencia

Lee la auditoría, investiga fuentes adicionales, aplica cambios autorizados, actualiza referencias y documenta limitaciones.

### Revisión humana

Confirma decisiones clínicas, de seguridad, población objetivo y aplicabilidad práctica. No debe aceptar automáticamente una recomendación solo porque tenga una cita.

## Archivos recomendados para cada tema

- `tema.md`: documento educativo final.
- `auditoria-tema-AAAA-MM-DD.md`: informe del verificador.
- `ejecucion-tema-AAAA-MM-DD.md`: cambios, fuentes y pendientes del investigador.
- `docs/referencia.bib`: referencia normalizada.
- `docs/bibliografia.md`: índice temático y criterios de selección.

## Criterio de salida

Un tema está listo para publicación solo si:

1. La pregunta y la población están delimitadas.
2. Las afirmaciones importantes tienen respaldo trazable.
3. Las cifras y recomendaciones tienen contexto.
4. Las limitaciones y el estado de acceso están declarados.
5. La revisión humana se completó cuando era necesaria.
6. La reauditoría no encuentra errores críticos o altos sin tratamiento.

Si alguno de estos puntos falla, el tema debe quedar como `Pendiente`, `Ejecución parcial` o `Requiere revisión`.

## Relación con los agentes del proyecto

- [Instrucciones del verificador](../../.agent/verificador-verdad-deportiva.md)
- [Instrucciones del investigador-ejecutor](../../.agent/investigador-ejecutor-evidencia.md)
- [Auditoría consolidada de referencia](../../auditoria-verificador-2026-10-04.md)
