---
name: academic-research
description: Investiga literatura academica de forma trazable para este repositorio documental: delimita preguntas, localiza y verifica fuentes, evalua acceso y evidencia, y prepara cambios prudentes con citas y BibTeX sincronizados.
license: Apache-2.0
compatibility: opencode
metadata:
  language: es
  domain: sports-science-documentation
  source: plurigrid/asi-academic-research
---

# Investigacion academica para OpenCode

Usa este skill para revisiones de literatura, auditorias de citas y correcciones de
`docs/`. Esta version adapta el skill `academic-research` de
`plurigrid/asi` al runtime de OpenCode y a las reglas de este repositorio.

## Capacidades reales en esta instalacion

### Disponibles

- `webfetch`: consultar PubMed, Europe PMC, Crossref, DOI, editoriales,
  repositorios institucionales y organismos oficiales mediante URLs directas.
- `grep` y `glob`: inventariar afirmaciones, citas, archivos y referencias locales.
- `read`: leer documentos, auditorias y archivos bibliograficos sin asumir que una
  referencia local es correcta.
- `bash`: ejecutar comprobaciones puntuales y comandos no destructivos, solo cuando
  aporten una verificacion reproducible.
- `task`: delegar investigacion independiente o una auditoria separada cuando el
  trabajo sea grande; el resultado debe volver con fuentes y limitaciones concretas.
- `apply_patch`: editar documentos y referencias de forma localizada.
- `headroom`, `serena` y otros MCP configurados: utilidades de contexto, proyecto y
  edicion; no son bases de datos academicas.
- MCP locales de este proyecto: `academic-semantic-scholar` (Semantic Scholar
  `1.0.2`), `academic-arxiv` (arXiv `1.1.0`) y `academic-pdf` (PDF server `2.0.3`).

### No disponibles salvo configuracion explicita

No inventes llamadas a estas herramientas ni afirmes que estan instaladas:

- `paper-search` para busqueda multi-fuente y BibTeX.
- `research-hub-mcp`, `zotero-mcp`, `openalex-mcp`, `crossref-mcp` o Unpaywall.
- Descarga automatica y persistente de PDFs como capacidad garantizada.

Semantic Scholar y arXiv tienen limites de acceso anonimo y solo exponen las
operaciones que ofrece la version instalada. Si una tarea necesita una capacidad
ausente, usa las URLs oficiales con `webfetch`, marca el alcance como limitado o pide
configurar otro MCP. No presentes una búsqueda manual como si hubiera sido una
búsqueda exhaustiva en todas las bases.

## Reglas del repositorio

Antes de investigar, lee `AGENTS.md`, la auditoria mas reciente y los documentos
relevantes de `docs/`. Para este proyecto, la auditoria consolidada actual es
`auditoria-verificador-2026-10-04.md`.

- Delimita pregunta, poblacion, intervencion o exposicion, comparador, resultados,
  contexto y exclusiones antes de buscar.
- Prioriza fuentes primarias, revisiones sistematicas, metaanalisis, consensos,
  guias y organismos oficiales.
- No uses blogs, redes, Wikipedia, snippets de buscador ni contenido generado por IA
  como evidencia final.
- Confirma DOI, PMID, PMCID u otro identificador en una fuente independiente.
- Separa resultado de la fuente, interpretacion y aplicacion practica.
- No conviertas rangos, ejemplos o heuristicas en protocolos universales.
- Si no puedes confirmar un dato, escribe `No verificado` o deja la afirmacion
  pendiente. No completes metadatos por similitud.
- Mantén el alcance en adultos sanos y poblaciones recreativas salvo delimitacion
  explicita. No hagas recomendaciones clinicas individualizadas.
- Para dolor, lesiones, embarazo, enfermedad, medicacion, suplementos, seguridad o
  baja disponibilidad energetica, conserva advertencias y solicita revision humana.

## Flujo de trabajo

### 1. Preparar la pregunta y el estado inicial

1. Define PICO o PECO y las exclusiones.
2. Lista las afirmaciones materiales que deben comprobarse, separando numeros,
   dosis, duraciones, umbrales, causalidad y recomendaciones.
3. Lee la auditoria mas reciente y ordena los hallazgos por severidad.
4. Comprueba cambios locales antes de editar; no sobrescribas trabajo ajeno.

### 2. Buscar por capas

Usa `webfetch` sobre fuentes directas, en este orden:

1. Revisiones sistematicas y metaanalisis para preguntas generales.
2. Consensos, guias y documentos de posicion.
3. Estudios primarios para dosis, poblaciones, protocolos y resultados concretos.
4. PubMed, Europe PMC, Crossref, DOI, editorial o repositorio institucional para
   confirmar identidad y metadatos.

Cuando sea util, consulta APIs oficiales con URLs codificadas. Ejemplos de rutas:

- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...`
- `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json`
- `https://api.crossref.org/works?query.bibliographic=...`

Una respuesta de API identifica una fuente; no demuestra que respalde la afirmacion
ni que su texto completo sea abierto.

### 3. Verificar cada fuente

Registra para cada fuente:

- autores, titulo, revista u organismo y año;
- DOI, PMID, PMCID u otro identificador;
- diseño, poblacion, muestra, nivel de entrenamiento y contexto;
- intervencion, comparador, dosis, frecuencia y duracion;
- resultado, magnitud e incertidumbre cuando esten disponibles;
- limitaciones, sesgos, conflictos de interes y aplicabilidad;
- URL legal y fecha de comprobacion.

Clasifica por separado la relacion entre fuente y afirmacion como `Directa`,
`Indirecta`, `Contradictoria` o `Ausente`. Clasifica el acceso como `Enlace roto`,
`Registro accesible`, `Texto completo accesible`, `Descarga verificable`, `Acceso
restringido` o `Acceso no comprobable`.

No confundas DOI o PubMed con acceso abierto. No descargues copias piratas ni
guardes binarios en el repositorio sin un lugar y una justificacion explicitos.

### 4. Analizar antes de editar

Para cada hallazgo documenta:

- afirmacion concreta y archivo/seccion;
- fuente que la confirma o contradice;
- razon por la que la evidencia es directa o indirecta;
- cambio exacto propuesto;
- limitaciones y riesgo residual.

No conviertas asociacion en causalidad, diferencia estadistica en beneficio importante
ni resultados de atletas entrenados en prescripcion para principiantes.

### 5. Aplicar cambios trazables

Cuando el usuario autorice la edicion:

- corrige primero errores bibliograficos criticos y hallazgos altos;
- añade citas inline junto a afirmaciones materiales;
- rebaja cifras y reglas a rangos orientativos si la evidencia no fija un umbral;
- mantiene sincronizados `docs/bibliografia.md` y `docs/referencia.bib`;
- no borra referencias validas no relacionadas;
- conserva estructura y tono educativo;
- marca como pendiente lo que no pueda confirmarse.

### 6. Reauditar

Relee cada cambio contra la fuente. Comprueba identificadores, enlaces, duplicados,
contradicciones entre documentos, citas sin respaldo y estado de acceso. Entrega una
tabla de hallazgos `resueltos`, `parcialmente resueltos` y `pendientes`, y solicita
reauditoria cuando proceda.

## Salida obligatoria

Entrega el informe en espanol con estas secciones:

1. `Resumen de ejecucion`: auditoria usada, fecha y alcance.
2. `Hallazgos atendidos`: severidad, fuentes, analisis, cambio y estado.
3. `Fuentes investigadas`: referencia, identificadores, evidencia, URL, acceso,
   descarga y fecha.
4. `Cambios en docs`: archivos y secciones modificadas.
5. `Pendientes`: bloqueos, fuentes no verificadas y revision humana necesaria.
6. `Recomendaciones de mejora`.
7. `Solicitud de reauditoria`.

Termina con exactamente uno de: `Ejecucion completa`, `Ejecucion parcial` o
`Bloqueado`. Nunca declares analizado, descargado o corregido algo que no hayas
comprobado.

## Configuracion opcional de MCP

Si el usuario pide ampliar la cobertura, puede añadir servidores academicos a la
configuracion de OpenCode. Antes de usarlos, comprueba que el servidor responde y
registra su version o fecha. La instalacion de un MCP no forma parte de este skill y
requiere autorizacion separada.

La ausencia de esos servidores no bloquea una investigacion acotada: `webfetch` puede
consultar registros y textos legales directamente, con la limitacion de no ofrecer
por si solo busqueda federada, grafo de citas ni gestion bibliografica.
