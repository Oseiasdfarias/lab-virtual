/* ****************************************************
 *
 * Universidade Federal do Pará
 * Campus Universitário de Tucuruí
 * Faculdade de Engenharia Elétrica
 * Trabalho de Conclusão de Curso - Aeropêndulo
 * Título : Firmware Potótipo Aeropêndulo
 *
 * Professor Orientador: Raphael Teixeira
 * Autor  : Oséias Farias
 *
 * Arquivo: main.cpp - Data: 2023
 *
 ****************************************************** */
#include <math.h>
#include "Arduino.h"

class Conversor
{
public:
    float converte_escala(float x_converter, float x_min, float x_max,
                          float y_min, float y_max, float offset);
    float converte_tensao_ciclo(float sinal_controle);
    float grau2rad(float angulo);
    float rad2grau(float angulo);
};

float Conversor::converte_escala(float x_converter, float x_min, float x_max,
                                 float y_min, float y_max, float offset)
{
    float m, F, x_conv, offset_conv;

    if (abs(x_converter) > x_max)
        m = abs(x_converter) / x_max;
    else
        m = 1.0;
    F = (y_min - y_max) / (x_min - x_max);
    if (x_converter < x_min)
    {
        if (x_converter < -x_max)
            x_converter = -x_max;
        x_conv = m * (((x_converter - x_min) * F) - y_min);
    }
    else
    {
        if (x_converter > x_max)
            x_converter = x_max;
        x_conv = m * (((x_converter - x_min) * F) + y_min);
    }
    offset_conv = ((offset - x_min) * F) + y_min;
    x_conv = x_conv - offset_conv;
    return x_conv;
}

float Conversor::converte_tensao_ciclo(float sinal_controle)
{
    // "0.0 <= sinal_controle <= 3.3" nao faz o que parece em C++: e avaliado
    // como "(0.0 <= sinal_controle) <= 3.3", ou seja, um bool (0 ou 1)
    // comparado a 3.3 -- sempre verdadeiro. Isso deixava o clamp de 255
    // inalcancavel e nao limitava valores negativos.
    int ciclo_trabalho = 0; // Ciclo de trabalho.
    if (sinal_controle <= 0.0)
        ciclo_trabalho = 0;
    else if (sinal_controle >= 3.3)
        ciclo_trabalho = 255;
    else
        ciclo_trabalho = (sinal_controle * 255.0) / 3.3;
    return ciclo_trabalho;
}

float Conversor::grau2rad(float angulo)
{
    return angulo * (M_PI / (float)180.0);
}

float Conversor::rad2grau(float angulo)
{
    return (float)180.0 * (M_PI / angulo);
}