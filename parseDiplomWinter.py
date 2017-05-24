import csv

questions = ['Sur le rayon j\'ai une boîte avec une couverture que Pierre a vernie.',
             'Maria a fait une ceinture de laine que Pierre a beaucoup aimée.',
             'Le prof parlait avec un parent d\'un garçon qui était à l\'hôpital.',
             'Hier, nous avons mangé un gâteau de riz qu\'on nous a vendu dans un magasin oriental.',
             'Durant la réunion, le chef du protocole a tenté de parler à un traducteur d\'un ambassadeur qui n\'a pas eu une invitation à la soirée.',
             'Le journaliste avait interviewé un fils d\'un colonel qui avait été dans un accident.', 'Tous nos amis ont aimé un oncle d\'un étudiant d\'échange qui nous rendait visite.', 'Le mois prochain on va envoyer à l\'étranger un secrétaire d\'un gérant qui fait des heures supplémentaires au bureau.', 'Ce matin j\'ai rencontré un oncle d\'un mécanicien qui habite dans le bâtiment où j\'habite.', 'On a accordé de replacer dans un autre bâtiment un ordinateur avec un moniteur que nous avions acheté récemment.', 'Laure a perdu un carnet avec un sticker que Pierre lui a donné.', 'À ma sœur, ils ont donné un bol d\'albâtre qu\'ils ont poli jusquà qu\'il soit pareil au marbre.', 'La police a arrêté un cousin d\'un peintre qui était à Marbella.', 'Hier ils m\'ont donné un pull de coton qui était importé illégalement.', 'Plusieurs malades ont aimé un infirmier d\'un chirurgien qui vient de commencer à travailler dans l\'hôpital.', 'Je voudrais prendre une radio avec une enceinte acoustique que j\'ai achetée à bas prix.', 'L\'explosion a rendu sourd un assistant d\'un inspecteur qui était non loin du magasin.', 'Le portier parlait à une sœur d\'une nurse qui était une amie de ma mère.', 'Dans le garage nous avons un tabouret en bois que Jean a taillé pendant ce weekend de Noël.', 'Le comte a demandé un steak avec une sauce que le chef prépare particulièrement bien.', 'Je parlais à un apprenti d\'un tailleur qui était à Paris peu de temps.', 'Enfin ils ont placé un timbre de bronze qu\'ils avaient pris dans une fonderie.', 'J\'ai apporté au bijoutier un bracelet avec un rubis que j\'avais acheté en Colombie.', 'Hier j\'ai vu un conseilleur d\'un directeur qui était triste à cause de la réponse misérable à la dernière promotion commerciale.']

final_questions = ['Qu\'est-ce que Pierre a verni?', 'Qu\'est-ce que Pierre a beaucoup aimé?', 'Qui était à l\'hôpital?', 'Qu\'est-ce qu\'on nous a vendu dans un magasin oriental?', 'Qui n\'a pas eu une invitation à la soirée?', 'Qui avait été dans un accident?', 'Qui nous rendait visite?', 'Qui fait des heures supplémentaires au bureau?', 'Qui habite dans le bâtiment où j\'habite?', 'Qu\'est-ce que nous avions acheté récemment?', 'Qu\'est-ce que Pierre a donné à Laure?', 'Qu\'est-ce qui est pareil au marbre?', 'Qui était à Marbella?', 'Qu\'est-ce qui était importé illégalement?', 'Qui vient de commencer à travailler dans l\'hôpital?', 'Qu\'est-ce que j\'ai acheté à bas prix?', 'Qui était non loin du magasin?', 'Qui était une amie de ma mère?', 'Qu\'est-ce que Jean a taillé pendant ce weekend de Noël?', 'Qu\'est-ce que le chef prépare particuièlerement bien?', 'Qui était à Paris peu de temps?', 'Qu\'est-ce qu\'ils avaient pris dans une fonderie?', 'Qu\'est-ce que j\'avais acheté en Colombie?', 'Qui était triste?']
with open('winterdata.csv', newline='', encoding='utf-8') as f:
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
