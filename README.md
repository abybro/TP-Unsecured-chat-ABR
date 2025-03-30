test
pickle peut etre dangeureux car Lors de la désérialisation, pickle peut exécuter du code arbitraire si la méthode __reduce__ d’un objet malveillant est définie. Cela permet à un attaquant d'exécuter des commandes sur le serveur.

ON pourrait utiliser Json qui est considéré plus sur


Le chiffrement garantit la confidentialité des données, mais il ne protège pas contre la modification des messages (intégrité) ni contre la falsification de l'origine du message (authenticité). Par exemple, un message chiffré pourrait être modifié en transit sans que la partie réceptrice ne le sache. Pour garantir l'intégrité et l'authenticité, il est nécessaire d'ajouter des mécanismes comme les signatures numériques ou les codes d'authentification de message (MAC).

 la fonction os.urandom() est utilisée pour générer un salt cryptographiquement sécurisé. 
 
 Oui, il faut transmettre le salt en clair avec le message, car il est nécessaire pour dériver la clé utilisée pour le chiffrement. Cependant, cela ne pose pas de problème de sécurité, car le salt n'a pas besoin d'être secret. Il sert simplement à rendre le processus de dérivation de la clé plus sécurisé et à éviter des attaques comme les attaques par dictionnaire.
 
 
Avec le AE_server et le AE_Client on peut remarquer maintenant que les données sont chiffrés et que l'on peut plus lire ce qu'envoie les gens.


Si le serveur est malveillant, il pourait modifier les messages avant de les transmettre aux clients. Comme :
Lire et stocker les messages avant de les transmettre / Modifier le contenu d’un message pour envoyer de fausses informations / Usurper l’identité d’un utilisateur en envoyant un message en son nom.

POur éviter une action de rogue server, on pourrait utiliser une signature numérique. Fernet n'est pas adapté car il ne garantit pas l'intégrité des messages. IL ne permet pas de vérifier que le message n'a pas été modifié en transit. Donc rogue peut modifier le message avant de le retransmettre sans que le destinataire le voit.
