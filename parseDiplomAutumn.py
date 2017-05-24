import csv

questions = ['Le mois prochain on va envoyer à l\'étranger le secrétaire du gérant qui fait des heures supplémentaires au bureau.',
             'Je voudrais prendre la radio avec l\'enceinte acoustique que j\'ai achetée à bas prix.',
             'J\'ai apporté au bijoutier le bracelet avec le rubis que j\'avais acheté en Colombie.',
             'La police a arrêté le cousin du peintre qui était à Marbella.',
             'Plusieurs malades ont aimé l\'infirmier du chirurgien qui vient de commencer à travailler dans l\'hôpital.',
             'Le comte a demandé le steak avec la sauce que le chef prépare particulièrement bien.', 'À ma sœur, ils ont donné le bol d\'albâtre qu\'ils ont poli jusqu\'à qu\'il soit pareil au marbre.', 'Sur le rayon j\'ai la boîte avec la couverture que Pierre a vernie.', 'Ce matin j\'ai rencontré l\'oncle du mécanicien qui habite dans le bâtiment où j\'habite.', 'Le portier parlait à la sœur de la nurse qui était une amie de ma mère.', 'Hier ils m\'ont donné le pull de coton qui était importé illégalement.', 'Je parlais à l\'apprenti du tailleur qui était à Paris peu de temps.', 'Tous nos amis ont aimé l\'oncle de l\'étudiant d\'échange qui nous rendait visite.', 'Dans le garage nous avons le tabouret en bois que Jean a taillé pendant ce weekend de Noël.', 'Hier j\'ai vu le conseilleur du directeur qui était triste à cause de la réponse misérable à la dernière promotion commerciale.', 'Laure a perdu le carnet avec le sticker que Pierre lui a donné.', 'Le journaliste avait interviewé le fils du colonel qui avait été dans un accident.', 'Durant la réunion, le chef du protocole a tenté de parler au traducteur de l\'ambassadeur qui n\'a pas eu une invitation à la soirée.', 'L\'explosion a rendu sourd l\'assistant de l\'inspecteur qui était non loin du magasin.', 'Le prof parlait avec le parent du garçon qui était à l\'hôpital.', 'Hier, nous avons mangé le gâteau de riz qu\'on nous a vendu dans un magasin oriental.', 'On a accordé de replacer dans un autre bâtiment l\'ordinateur avec le moniteur que nous avions acheté récemment.', 'Enfin ils ont placé le timbre de bronze qu\'ils avaient pris dans une fonderie.', 'Maria a fait la ceinture de laine que Pierre a beaucoup aimée.']

final_questions = ['Qui fait des heures supplémentaires au bureau?', 'Qu\'est-ce que j\'ai acheté à bas prix?', 'Qu\'est-ce que j\'avais acheté en Colombie?', 'Qui était à Marbella?', 'Qui vient de commencer à travailler dans l\'hôpital?', 'Qu\'est-ce que le chef prépare particuièlerement bien?', 'Qu\'est-ce qui est pareil au marbre?', 'Qu\'est-ce que Pierre a verni?', 'Qui habite dans le bâtiment où j\'habite?', 'Qui était une amie de ma mère?', 'Qu\'est-ce qui était importé illégalement?', 'Qui était à Paris peu de temps?', 'Qui nous rendait visite?', 'Qu\'est-ce que Jean a taillé pendant ce weekend de Noël?', 'Qui était triste?', 'Qu\'est-ce que Pierre a donné à Laure?', 'Qui avait été dans un accident?', 'Qui n\'a pas eu une invitation à la soirée?', 'Qui était non loin du magasin?', 'Qui était à l\'hôpital?', 'Qu\'est-ce qu\'on nous a vendu dans un magasin oriental?', 'Qu\'est-ce que nous avions acheté récemment?', 'Qu\'est-ce qu\'ils avaient pris dans une fonderie?', 'Qu\'est-ce que Pierre a beaucoup aimé?']
with open('autumndata.csv', newline='', encoding='utf-8') as f:
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
