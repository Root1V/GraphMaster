
Project: ...
=================

## Configuración

Antes de ejecutar la aplicación, asegúrate de configurar las siguientes variables de entorno:

file: \\\`.env\\\`

\\\`\\\`\\\`bash
    OPENAI_API_KEY=
    GROQ_API_KEY=
    ANTHROPIC_API_KEY=
    GEMINI_API_KEY=
\\\`\\\`\\\`

## Ejecución

Para ejecutar la aplicación, simplemente usa el siguiente comando:

\\\`\\\`\\\`bash
python app.py
\\\`\\\`\\\`

Namespace TeoriaGrafos
======================

Sub-modules
-----------
* TeoriaGrafos.app
* TeoriaGrafos.main


Module TeoriaGrafos.app.app
===========================

Classes
-------

`App()`
:

    ### Methods

    `generate_text(self, prompt)`
    :   Generar texto con el modelo LLM GTP-4o-mini


Module TeoriaGrafos.app.config
==============================

Classes
-------

`Config()`
:

    ### Static methods

    `get_all(filepath='app/config-model.json')`
    :   Carga y devuelve todos los valores del archivo config-model.json.


Module TeoriaGrafos.main
========================
