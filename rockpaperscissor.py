import random

rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
questions = {1: {'question': 'What is the capital of France?', 'choices': {'A': 'paris', 'B': 'london'}, 'answer': 'A'},
             2: {'question': 'What is the highest mountain in the world?', 'choices': {'A': 'mount everest', 'B': 'kilimanjaro'}, 'answer': 'A'},
             3: {'question': 'Who invented the telephone?', 'choices': {'A': 'thomas edison', 'B': 'alexander graham bell'}, 'answer': 'B'}}
fun_facts = {1: 'Poverty disproportionately affects women, children, and marginalized groups, such as indigenous peoples and refugees.',
             2: 'Poverty is not just about a lack of income; it also involves limited access to basic services, such as education, healthcare, and clean water and sanitation.',
             3: 'Poverty can perpetuate a cycle of disadvantage and exclusion, making it difficult for individuals and communities to break free from poverty.',
             4: 'Achieving SDG 1 will require a comprehensive approach that addresses the root causes of poverty, such as inequality, discrimination, and lack of access to basic services and opportunities.',
             5: 'In 2020, around 9.2 percent of the global population lived in extreme poverty, which means they had to survive on less than $1.90 per day.',
             6: 'Around 690 million people around the world suffer from hunger, meaning they do not have enough food to meet their basic nutritional needs.',
             7: 'The majority of people affected by hunger live in developing countries, particularly in sub-Saharan Africa and Southern Asia.',
             8: 'Hunger is not just about a lack of food; it is also linked to poverty, inequality, conflict, and climate change.',
             9: 'Malnutrition is a major global health challenge, affecting 1 in 3 people worldwide and contributing to stunted growth, impaired cognitive development, and increased vulnerability to disease.',
             10: 'Achieving SDG 2 will require a range of actions, including promoting sustainable agriculture, improving food systems and supply chains, increasing access to nutritious and affordable food, and addressing the root causes of hunger and malnutrition.',
             11: 'Many people around the world still lack access to basic healthcare services.',
             12: 'Non-communicable diseases such as heart disease, cancer, and diabetes are now the leading causes of death worldwide.',
             13: 'Mental health is an important aspect of overall health and well-being, and it is a major global health challenge.',
             14: 'Achieving universal health coverage is a key goal',
             15: 'Investing in health and well-being can have significant economic benefits, including reducing poverty and promoting economic growth.',
             16: 'Access to education is a basic human right and an important tool for promoting development.',
             17: 'Quality education helps to reduce poverty, promote gender equality, and foster economic growth.',
             18: 'Despite progress in recent years, many children and youth still do not have access to education, particularly in low-income countries.',
             19: 'Girls and women face particular barriers to accessing education, including poverty, cultural norms, and gender-based violence.',
             20: 'Achieving SDG 4 will require significant investment in education, including expanding access to education, improving the quality of education, and ensuring that education is relevant to the needs of individuals and communities.',
             21: 'Gender equality is a fundamental human right, and it is essential for promoting sustainable development and ending poverty.',
             22: 'Despite progress in recent years, women and girls still face significant barriers to equality, including discrimination, violence, and unequal access to education, healthcare, and economic opportunities.',
             23: 'Empowering women and girls is a key component of achieving all of the SDGs, as women and girls play important roles in their families, communities, and economies.',
             24: 'Achieving gender equality requires the involvement of all members of society, including men and boys, as well as governments, civil society organizations, and the private sector.',
             25: 'Investing in gender equality can have significant economic benefits, including reducing poverty, promoting economic growth, and improving health and education outcomes for both women and men.',
             26: 'Access to clean water and sanitation is a fundamental human right, and it is essential for promoting public health, economic development, and environmental sustainability.',
             27: 'Despite progress in recent years, many people still do not have access to clean water and basic sanitation services, particularly in low-income countries and in rural areas.',
             28: 'Lack of access to clean water and sanitation can have significant negative impacts on health, education, and economic outcomes, particularly for women and girls.',
             29: 'Achieving SDG 6 will require significant investments in infrastructure, as well as improvements in water resource management, wastewater treatment, and hygiene practices.',
             30: 'SDG 6 is closely linked to other SDGs, including SDG 3 (Good Health and Well-being), SDG 5 (Gender Equality), and SDG 14 (Life Below Water), among others, highlighting the interconnectedness of the SDGs.',
             31: 'Access to affordable and clean energy is essential for achieving sustainable development, reducing poverty, and combating climate change.',
             32: 'Despite progress in recent years, many people still lack access to reliable and affordable energy, particularly in low-income countries and in rural areas.',
             33: 'Increasing the share of renewable energy in the global energy mix is essential for achieving SDG 7 and reducing greenhouse gas emissions.',
             34: 'SDG 7 also includes targets related to improving energy efficiency, expanding access to modern energy services, and enhancing international cooperation on energy issues.',
             35: 'Achieving SDG 7 will require significant investments in energy infrastructure, as well as policy and regulatory reforms to promote clean energy and energy access for all.',
             36: 'Promoting sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all are essential components of sustainable development.',
             37: 'Despite progress in recent years, the global economy still faces significant challenges, including persistent unemployment, underemployment, and inequality.',
             38: 'Achieving SDG 8 requires a focus on job creation, particularly in sectors that are most likely to spur growth and reduce poverty, such as manufacturing and technology.',
             39: 'SDG 8 also emphasizes the need to promote entrepreneurship and innovation, strengthen labor protections and social protections, and improve access to financial services.',
             40: 'Achieving SDG 8 will require significant investments in education and skills training, infrastructure, and technology, as well as policy and regulatory reforms to promote inclusive economic growth and decent work.',
             41: 'Investment in infrastructure and innovation are crucial drivers of economic growth and development.',
             42: 'In many parts of the world, infrastructure is inadequate or insufficient, particularly in low-income countries and in rural areas.',
             43: 'Enhancing access to technology and innovation is essential for achieving SDG 9, particularly for low-income and developing countries.',
             44: 'SDG 9 also emphasizes the importance of sustainable infrastructure development, including the use of renewable energy, sustainable transportation, and efficient building design.',
             45: 'Achieving SDG 9 will require significant investments in infrastructure, research and development, and technology transfer, as well as policy and regulatory reforms to promote sustainable and inclusive economic growth.',
             46: 'Inequalities exist within and between countries, and can manifest in various forms, including income, gender, race, ethnicity, disability, and migration status.',
             47: 'Reducing inequalities is critical for achieving sustainable development, as they can undermine social cohesion, political stability, and economic growth.',
             48: 'SDG 10 emphasizes the need to reduce inequalities in income, wealth, and opportunity, and to promote social, economic, and political inclusion for all.',
             49: 'Achieving SDG 10 requires addressing the root causes of inequalities, including discriminatory laws and policies, unequal access to education, healthcare, and other basic services, and inadequate social protections.',
             50: 'To achieve SDG 10, it is necessary to support developing countries, address migration challenges, including forced migration, protect migrants rights, and promote safe and orderly migration.',
             51: 'SDG 11 aims to make cities and human settlements inclusive, safe, resilient, and sustainable.',
             52: 'Sustainable cities and communities require integrated planning and management of urbanization, including the provision of affordable housing, infrastructure, and basic services.',
             53: 'SDG 11 also emphasizes the need to reduce the environmental impact of cities and human settlements, including air pollution, waste management, and sustainable transport.',
             54: 'Achieving SDG 11 requires the active participation of all stakeholders, including governments, civil society, private sector, and communities, to ensure sustainable and equitable urbanization.',
             55: 'The significance of sustainable cities and communities is emphasized by the projected increase in the urban population, which is expected to reach 68 percent by 2050.',
             56: 'Around one third of all food produced for human consumption is wasted every year, while millions of people suffer from hunger.',
             57: 'Global material consumption has more than tripled over the past 50 years, with natural resource extraction exceeding 92 billion tons in 2017.',
             58: 'Only 20 percent of electronic waste is formally recycled, while the rest ends up in landfills, incinerators or in the environment, causing severe pollution.',
             59: 'An estimated 1.3 billion tonnes of solid waste is generated every year, posing significant environmental and health risks.',
             60: 'Sustainable consumption and production practices can create new business opportunities, generate green jobs, and contribute to poverty reduction and climate change mitigation.',
             61: 'Climate change is one of the biggest challenges of our time and threatens to undo decades of development progress.',
             62: 'The impact of climate change is being felt worldwide, from rising sea levels to more frequent natural disasters and extreme weather events.',
             63: 'Developing countries are particularly vulnerable to the effects of climate change, despite contributing the least to the problem.',
             64: 'The Paris Agreement, which aims to limit global temperature rise to well below 2 degrees Celsius above pre-industrial levels, is a key international effort to address climate change.',
             65: 'To achieve SDG 13, urgent action is needed to reduce greenhouse gas emissions, promote renewable energy, and build resilience to the impacts of climate change.',
             66: 'Marine biodiversity is essential for maintaining the health of our planet and sustaining life on Earth.',
             67: 'Overfishing and illegal fishing practices have led to a decline in fish populations, threatening the livelihoods of millions of people who depend on fishing for their food and income.',
             68: 'Climate change is having a significant impact on oceans, causing sea level rise, ocean acidification, and changes in ocean currents, which can have a devastating effect on marine ecosystems.',
             69: 'SDG 14 aims to conserve and sustainably use oceans, seas, and marine resources for sustainable development, promoting actions to reduce pollution, protect marine ecosystems and biodiversity, and support sustainable fisheries.',
             70: 'The majority of the Earth surface is comprised of oceans, and within these immense bodies of water exists a diverse range of marine life, some of which have yet to be identified.',
             71: 'Forests cover 31 percent of the Earth land surface and are home to 80 percent of the world terrestrial biodiversity.',
             72: 'Over 25 percent of the world land is degraded, with soil erosion, deforestation, and desertification being major contributors.',
             73: 'Illegal wildlife trade is a multi-billion dollar industry, posing a significant threat to endangered species and the ecosystems they inhabit.',
             74: 'More than 2 billion people rely on traditional medicines, many of which are derived from plants and animals found in forests and other natural habitats.',
             75: 'The restoration of degraded forests and other natural habitats can help to mitigate climate change, protect biodiversity, and improve local livelihoods.',
             76: 'SDG 16 aims to promote peaceful and inclusive societies for sustainable development, provide access to justice for all, and build effective, accountable, and inclusive institutions at all levels.',
             77: 'Corruption, bribery, and other forms of illicit financial flows drain trillions of dollars from developing countries every year, hindering progress towards SDG 16.',
             78: 'Violence against children, women, and other vulnerable groups remains a significant problem worldwide, with over 1 billion children estimated to have experienced violence in the past year alone.',
             79: 'Ensuring access to justice for all, regardless of their income level or background, is crucial for promoting peaceful and inclusive societies, yet billions of people still lack access to basic justice services.',
             80: 'Inclusive and participatory decision-making processes that involve all members of society, including marginalized and vulnerable groups, are essential for building accountable institutions and promoting sustainable development.'}

def play_round(score, username):
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    while True:
        user_choice = input('Choose rock (1), paper (2), or scissors (3): ')
        if user_choice not in choices:
            print('Invalid choice!')
        else:
            user_choice = choices[user_choice]
            break

    # Draw the player's choice
    if user_choice == 'rock':
        print('You chose rock:')
        print('    _______')
        print('---\'   ____)')
        print('      (_____)')
        print('      (_____)')
        print('      (____)')
        print('---.__(___)')
    elif user_choice == 'paper':
        print('You chose paper:')
        print('     _______')
        print('---\'    ____)____')
        print('           ______)')
        print('          _______)')
        print('         _______)')
        print('---.__________)')
    elif user_choice == 'scissors':
        print('You chose scissors:')
        print('    _______')
        print('---\'   ____)____')
        print('          ______)')
        print('       __________)')
        print('      (____)')
        print('---.__(___)')

    computer_choice = random.choice(list(rules.keys()))

    # Draw the computer's choice
    if computer_choice == 'rock':
        print('Computer chose rock:')
        print('    _______')
        print('---\'   ____)')
        print('      (_____)')
        print('      (_____)')
        print('      (____)')
        print('---.__(___)')
    elif computer_choice == 'paper':
        print('Computer chose paper:')
        print('     _______')
        print('---\'    ____)____')
        print('           ______)')
        print('          _______)')
        print('         _______)')
        print('---.__________)')
    elif computer_choice == 'scissors':
        print('Computer chose scissors:')
        print('    _______')
        print('---\'   ____)____')
        print('          ______)')
        print('       __________)')
        print('      (____)')
        print('---.__(___)')

    if rules[user_choice] == computer_choice:
        print(f'You win! Here is a fun fact: {fun_facts[random.randint(1, 80)]}')
        score += 1
    elif rules[computer_choice] == user_choice:
        question = questions[random.randint(1, 3)]
        print('You lose! Here is a question:')
        print(question['question'])
        for key, value in question['choices'].items():
            print(f"{key.upper()}: {value}")
        user_answer = input('Answer: ').lower()
        if user_answer == question['answer'].lower():
            print('Correct! You get a point.')
            score += 1
        else:
            print('Incorrect! You lose a point.')
            score -= 1
    else:
        print('It\'s a tie!')
    print(f'{username} Score: {score}\n')
    return score

def play_game():
    players = []
    while True:
        print("Welcome to Rock-Paper-Scissors game!")
        print("Please choose an option:")
        print("1. Play\n2. How to play\n3. About\n4. Leaderboards\n5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            username = input('Enter your username: ')
            num_rounds = int(input('How many rounds do you want to play? '))
            user_score = 0
            for i in range(num_rounds):
                print(f'Round {i+1}:')
                user_score = play_round(user_score, username)
            players.append({'name': username, 'score': user_score})
            print(f'{username}, your final score: {user_score}/{num_rounds}\n')
        elif choice == '2':
            print("How to play:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")
        elif choice == '3':
            print("About:\nThis game was created by [Your Name]\n")
        elif choice == '4':
            print("Leaderboards:\n")
            sorted_players = sorted(players, key=lambda x: x['score'], reverse=True)
            for i, player in enumerate(sorted_players):
                print(f"{i+1}. {player['name']}: {player['score']}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")

    # Sort players by score in descending order
    sorted_players = sorted(players, key=lambda x: x['score'], reverse=True)
    print("Leaderboards:\n")
    for i, player in enumerate(sorted_players):
        print(f"{i+1}. {player['name']}: {player['score']}")


play_game()
