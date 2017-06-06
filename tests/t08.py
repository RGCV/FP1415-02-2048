## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                  TEST 08                                   ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Modifier: tabuleiro_reduz -- #
T = cria_tabuleiro()
C = cria_coordenada(1, 4)
T = tabuleiro_preenche_posicao(T, C, 2)
T = tabuleiro_reduz(T, 'W')
tabuleiro_pontuacao(T)
T = tabuleiro_preenche_posicao(T, C, 2)
T = tabuleiro_reduz(T, 'W')
tabuleiro_pontuacao(T)
# - (additional hidden tests) - #
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 2)
T = tabuleiro_reduz(T, 'W')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 2)
T = tabuleiro_reduz(T, 'E')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 2)
T = tabuleiro_reduz(T, 'W')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 2)
T = tabuleiro_reduz(T, 'N')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 2)
T = tabuleiro_reduz(T, 'S')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 4), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 3), 2)
T = tabuleiro_reduz(T, 'W')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 2)
T = tabuleiro_reduz(T, 'E')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 4)
T = tabuleiro_reduz(T, 'N')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 2), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 4), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 3), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 8)
T = tabuleiro_reduz(T, 'S')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 1), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 4), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 4)
T = tabuleiro_reduz(T, 'W')
escreve_tabuleiro(T)
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 16)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 2), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 3), 4)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 2)
T = tabuleiro_reduz(T, 'N')
T = tabuleiro_reduz(T, 'S')
T = tabuleiro_reduz(T, 'E')
T = tabuleiro_reduz(T, 'W')
escreve_tabuleiro(T)