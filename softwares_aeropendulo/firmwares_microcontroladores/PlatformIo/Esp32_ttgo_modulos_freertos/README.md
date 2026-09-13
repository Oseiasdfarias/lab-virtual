# Nota sobre o nome desta pasta

Apesar do nome, este firmware **não usa nenhuma API do FreeRTOS** (sem `xTaskCreate` ou
qualquer chamada equivalente) — roda em `loop()` single-task, igual às demais variantes.

A variante mais completa e atualizada é
[`../Esp32_ttgo_modulos`](../Esp32_ttgo_modulos/), que tem PID, seleção de forma de onda de
referência e alternância entre malha aberta/fechada. Esta pasta tem menos funcionalidade que
aquela.

Não renomeada para evitar quebrar caminhos já referenciados em outro lugar — mas não confie
no nome ao decidir qual variante usar.
