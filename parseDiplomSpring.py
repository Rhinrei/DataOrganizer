import csv

questions = ['Hier ils m\'ont donné un pull de coton qui était importé illégalement.',
             'Le mois prochain on va envoyer à l\'étranger un secrétaire du gérant qui fait des heures supplémentaires au bureau.',
             'On a accordé de replacer dans un autre bâtiment un ordinateur avec le moniteur que nous avions acheté récemment.', 'À ma sœur, ils ont donné un bol d\'albâtre qu\'ils ont poli jusqu\'à qu\'il soit pareil au marbre.', 'Le comte a demandé un steak avec la sauce que le chef prépare particulièrement bien.', 'L\'explosion a rendu sourd un assistant de l\'inspecteur qui était non loin du magasin.', 'Laure a perdu un carnet avec le sticker que Pierre lui a donné.', 'Hier j\'ai vu un conseilleur du directeur qui était triste à cause de la réponse misérable à la dernière promotion commerciale.', 'Le portier parlait à une sœur de la nurse qui était une amie de ma mère.', 'Le journaliste avait interviewé un fils du colonel qui avait été dans un accident.', 'Le prof parlait avec un parent du garçon qui était à l\'hôpital.', 'Sur le rayon j\'ai une boîte avec la couverture que Pierre a vernie.', 'La police a arrêté un cousin du peintre qui était à Marbella.', 'J\'ai apporté au bijoutier un bracelet avec le rubis que j\'avais acheté en Colombie.', 'Je parlais à un apprenti du tailleur qui était à Paris peu de temps.', 'Maria a fait une ceinture de laine que Pierre a beaucoup aimée.', 'Durant la réunion, le chef du protocole a tenté de parler à un traducteur de l\'ambassadeur qui n\'a pas eu une invitation à la soirée.', 'Enfin ils ont placé un timbre de bronze qu\'ils avaient pris dans une fonderie.', 'Je voudrais prendre une radio avec l\'enceinte acoustique que j\'ai achetée à bas prix.', 'Plusieurs malades ont aimé un infirmier du chirurgien qui vient de commencer à travailler dans l\'hôpital.', 'Tous nos amis ont aimé un oncle de l\'étudiant d\'échange qui nous rendait visite.', 'Dans le garage nous avons un tabouret en bois que Jean a taillé pendant ce weekend de Noël.', 'Hier, nous avons mangé un gâteau de riz qu\'on nous a vendu dans un magasin oriental.', 'Ce matin j\'ai rencontré un oncle du mécanicien qui habite dans le bâtiment où j\'habite.']

final_questions = ['Qu\'est-ce qui était importé illégalement?', 'Qui fait des heures supplémentaires au bureau?', 'Qu\'est-ce que nous avions acheté récemment?', 'Qu\'est-ce qui est pareil au marbre?', 'Qu\'est-ce que le chef prépare particuièlerement bien?', 'Qui était non loin du magasin?', 'Qu\'est-ce que Pierre a donné à Laure?', 'Qui était triste?', 'Qui était une amie de ma mère?', 'Qui avait été dans un accident?', 'Qui était à l\'hôpital?', 'Qu\'est-ce que Pierre a verni?', 'Qui était à Marbella?', 'Qu\'est-ce que j\'avais acheté en Colombie?', 'Qui était à Paris peu de temps?', 'Qu\'est-ce que Pierre a beaucoup aimé?', 'Qui n\'a pas eu une invitation à la soirée?', 'Qu\'est-ce qu\'ils avaient pris dans une fonderie?', 'Qu\'est-ce que j\'ai acheté à bas prix?', 'Qui vient de commencer à travailler dans l\'hôpital?', 'Qui nous rendait visite?', 'Qu\'est-ce que Jean a taillé pendant ce weekend de Noël?', 'Qu\'est-ce qu\'on nous a vendu dans un magasin oriental?', 'Qui habite dans le bâtiment où j\'habite?']
with open('springdata.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    spamWriter = csv.writer(open('res.csv', 'w', newline='', encoding='utf-8'), delimiter=';')
    i = 1
    # ['nnumb', 'IP adress', 'Level'] +  ['Usloviye']
    spamWriter.writerow(['Number', 'IP adress', 'Level'] + questions + ['Experiment List'])
    for row in reader:
        if row['завершённый ответ'] != '' and row['Votre niveau de français:'] != "locuteur natif":
            result_row = [i, row['IP адрес'], row['Votre niveau de français:']]

            answers = []
            for q in final_questions:
                answers.append(row[q])

            result_row += answers
            result_row.append('un - un')

            spamWriter.writerow(result_row)
            i += 1
