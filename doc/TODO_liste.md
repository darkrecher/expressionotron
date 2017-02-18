# TODO liste

## Code à nettoyer

Fichier : `repo_git/expressionotron/server/mysite/expressionotron/v002/seeder.py`

À priori, cette ligne de code ne sert à rien : `total_length //= data_index_length`.

Ce sera corrigé et testé à la prochaine version. Là, j'ai la flemme de rechanger le code et de mettre à jour le site juste pour ça.


## Vérification du paramètre lors du "POST"

Mentionné ici : `repo_git/expressionotron/doc/doc_conception.md`

La fonction `expressionotron_post` est associée à la méthode HTTP "POST". Le paramètre `unsafe_expr_gen_key` est récupéré depuis le paramètre de formulaire "seedInForm".

Comme c'est un POST, ce paramètre est censé être toujours présent. S'il ne l'est pas, une exception est levée et le résultat final est une erreur HTTP 400. J'aurais pu faire en sorte que ce cas soit mieux géré, mais il n'y a que maintenant que je le découvre. Tant pis, ce sera pour la prochaine version !
