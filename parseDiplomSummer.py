import csv

questions = ['Le mois prochain on va envoyer à l\'étranger le secrétaire d\'un gérant qui fait des heures supplémentaires au bureau.',
             'Enfin ils ont placé le timbre de bronze qu\'ils avaient pris dans une fonderie.',
             'Le comte a demandé le steak avec une sauce que le chef prépare particulièrement bien.',
             'J\'ai apporté au bijoutier le bracelet avec un rubis que j\'avais acheté en Colombie.',
             'Ce matin j\'ai rencontré l\'oncle d\'un mécanicien qui habite dans le bâtiment où j\'habite.',
             'Maria a fait la ceinture de laine que Pierre a beaucoup aimée.', 'Durant la réunion, le chef du protocole a tenté de parler au traducteur d\'un ambassadeur qui n\'a pas eu une invitation à la soirée.', 'L\'explosion a rendu sourd l\'assistant d\'un inspecteur qui était non loin du magasin.', 'Plusieurs malades ont aimé l\'infirmier d\'un chirurgien qui vient de commencer à travailler dans l\'hôpital.', 'La police a arrêté le cousin d\'un peintre qui était à Marbella.', 'Hier, nous avons mangé le gâteau de riz qu\'on nous a vendu dans un magasin oriental.', 'Hier ils m\'ont donné le pull de coton qui était importé illégalement.', 'Je parlais à l\'apprenti d\'un tailleur qui était à Paris peu de temps.', 'Le portier parlait à la sœur d\'une nurse qui était une amie de ma mère.', 'Hier j\'ai vu le conseilleur d\'un directeur qui était triste à cause de la réponse misérable à la dernière promotion commerciale.', 'Laure a perdu le carnet avec un sticker que Pierre lui a donné.', 'Sur le rayon j\'ai la boîte avec une couverture que Pierre a vernie.', 'Tous nos amis ont aimé l\'oncle d\'un étudiant d\'échange qui nous rendait visite.', 'À ma sœur, ils ont donné le bol d\'albâtre qu\'ils ont poli jusqu\'à qu\'il soit pareil au marbre.', 'Le journaliste avait interviewé le fils d\'un colonel qui avait été dans un accident.', 'Je voudrais prendre la radio avec une enceinte acoustique que j\'ai achetée à bas prix.', 'Dans le garage nous avons le tabouret en bois que Jean a taillé pendant ce weekend de Noël.', 'On a accordé de replacer dans un autre bâtiment l\'ordinateur avec un moniteur que nous avions acheté récemment.', 'Le prof parlait avec le parent d\'un garçon qui était à l\'hôpital.']

final_questions = ['Qui fait des heures supplémentaires au bureau?', 'Qu\'est-ce qu\'ils avaient pris dans une fonderie?', 'Qu\'est-ce que le chef prépare particuièlerement bien?', 'Qu\'est-ce que j\'avais acheté en Colombie?', 'Qui habite dans le bâtiment où j\'habite?', 'Qu\'est-ce que Pierre a beaucoup aimé?', 'Qui n\'a pas eu une invitation à la soirée?', 'Qui était non loin du magasin?', 'Qui vient de commencer à travailler dans l\'hôpital?', 'Qui était à Marbella?', 'Qu\'est-ce qu\'on nous a vendu dans un magasin oriental?', 'Qu\'est-ce qui était importé illégalement?', 'Qui était à Paris peu de temps?', 'Qui était une amie de ma mère?', 'Qui était triste?', 'Qu\'est-ce que Pierre a donné à Laure?', 'Qu\'est-ce que Pierre a verni?', 'Qui nous rendait visite?', 'Qu\'est-ce qui est pareil au marbre?', 'Qui avait été dans un accident?', 'Qu\'est-ce que j\'ai acheté à bas prix?', 'Qu\'est-ce que Jean a taillé pendant ce weekend de Noël?', 'Qu\'est-ce que nous avions acheté récemment?', 'Qui était à l\'hôpital?']
with open('summerdata.csv', newline='', encoding='utf-8') as f:
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
