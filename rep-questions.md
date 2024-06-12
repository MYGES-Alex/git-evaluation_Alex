Réponses aux questions
Git est un gestionnaire de version décentralisé. Qu’est ce que cela signifie ? Quel est le rôle joué par un dépôt central sur GitHub ou GitLab dans ce cas ? Justifier.

Un gestionnaire de version décentralisé signifie que chaque utilisateur possède une copie complète de l'historique du dépôt, permettant des opérations hors ligne. Un dépôt central comme GitHub ou GitLab sert de point de synchronisation pour partager les modifications avec d'autres utilisateurs et faciliter la collaboration.

À quoi sert la commande git fetch -p ?

La commande git fetch -p (prune) supprime les branches distantes qui n'existent plus sur le dépôt distant.

Dans quelles conditions est-ce qu’un conflit apparaît avec git ?

Un conflit apparaît lorsque des modifications concurrentes sont apportées à la même ligne d'un fichier ou lorsqu'une branche a des commits que l'autre branche ne possède pas.

Lorsque vous résolvez un conflit, quelle est la dernière commande git que vous devez exécuter ?

Après avoir résolu un conflit, la commande git commit doit être exécutée pour finaliser la résolution du conflit.

Depuis GitHub, après avoir accepté une contribution sur la branche principale, que devez vous faire pour mettre à jour votre branche principale localement ?

Il faut exécuter git pull origin main pour mettre à jour la branche principale locale avec les modifications du dépôt distant.

Quelle est la différence entre les commandes git reset --soft et git reset --hard ? Donner un cas d’usage pratique et courant pour chacune de ces commandes.

git reset --soft <commit> conserve les modifications dans l'index et le répertoire de travail, utile pour modifier l'historique des commits. git reset --hard <commit> réinitialise l'index et le répertoire de travail, utile pour annuler des changements indésirables.

Voici le log d’un dépôt git : Quelle est la (ou les) commande à exécuter pour transformer les commits 9f64652 et 68cd016 en un seul commit avec un nouveau message ?

Utilisez git rebase -i d47267f puis dans l'éditeur, changez pick pour squash pour le commit 68cd016 et modifiez le message de commit.

Pourquoi est-il déconseillé de rebase une branche publique (branche sur laquelle travaille aussi d’autres personnes) ?

Parce que cela réécrit l'historique des commits, causant des incohérences et des conflits pour les autres utilisateurs ayant la même branche.