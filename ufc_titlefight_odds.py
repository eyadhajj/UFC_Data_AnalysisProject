import pandas as pd
import matplotlib.pyplot as mpl

data = pd.read_csv("C:\\Users\\Administrator\\Desktop\\Coding\\Python\\UFC Data Analysis\\Title-OddsWinRate\\ufc-master.csv")


total_fights = data['title_bout'].count()


title_fights = data[data['title_bout'] == True]
title_fights_count = title_fights['title_bout'].sum()


# Uncomment the class to see data.

# class Title_Nontitle():
#     labels = ['Title Fights', 'Non-Title Fights']
#     sizes = [title_fights_count, total_fights - title_fights_count]

#     mpl.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

#     mpl.axis('equal')

#     mpl.title("Title Fights vs Non-Title Fights in the UFC (2010 - 2021)")

#     mpl.show()

# class glove_c_winrate():

#     instance = 0

#     for index, row in data.iterrows():
#             if (row['Winner'] == 'Red' and row['title_bout'] == True):
#                 instance = instance + 1


#     instance_b = 0

#     for index, row in data.iterrows():
#             if (row['Winner'] == 'Blue' and row['title_bout'] == True):
#                 instance_b = instance_b + 1

#     colors = ['skyblue', 'lightcoral']  # Specify colors for each slice
#     label_distance = 0.7
#     labels_2 = ['Red Gloves', 'Blue Gloves']
#     sizes_2 = [instance, instance_b]

#     mpl.pie(sizes_2, labels=labels_2, autopct='%1.1f%%', startangle=143, colors=colors, labeldistance=label_distance)

#     mpl.axis('equal')

#     mpl.title("Championship fights: Win ratio bettween glove colours")

#     mpl.show()

# class alex_vol_stance():

#     # Filter data for fights involving Alexander Volkanovski
#     volkanovski_fights = data[(data['R_fighter'] == 'Alexander Volkanovski') | (data['B_fighter'] == 'Alexander Volkanovski')]

#     # Extract unique stances from both red and blue corner for Volkanovski's fights
#     stances = set(volkanovski_fights['R_Stance'].unique()).union(set(volkanovski_fights['B_Stance'].unique()))

#     # Remove any NaN values from the set
#     stances.discard(float("nan"))

#     # Count the occurrences of each stance
#     stance_counts = {}
#     for stance in stances:
#         stance_counts[stance] = volkanovski_fights[(volkanovski_fights['R_Stance'] == stance) | (volkanovski_fights['B_Stance'] == stance)].shape[0]

#     # Plotting the pie chart
#     mpl.figure(figsize=(8, 8))
#     mpl.pie(stance_counts.values(), labels=stance_counts.keys(), autopct='%1.1f%%', startangle=140)
#     mpl.title("Stances Used by Alexander Volkanovski")
#     mpl.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#     mpl.show()

# class stances():
    
#     southpaw_win_inst = 0

#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Southpaw' and row['Winner'] == 'Blue') or (row['R_Stance'] == 'Southpaw'and row['Winner'] == 'Red'):
#                 southpaw_win_inst += 1

#     southpaw_loss_inst = 0

#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Southpaw' and row['Winner'] == 'Red') or (row['R_Stance'] == 'Southpaw'and row['Winner'] == 'Blue'):
#                 southpaw_loss_inst += 1



#     orthodox_win_inst = 0

#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Orthodox' and row['Winner'] == 'Blue') or (row['R_Stance'] == 'Orthodox' and row['Winner'] == 'Red'):
#                 orthodox_win_inst += 1

#     orthodox_loss_inst = 0
#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Orthodox' and row['Winner'] == 'Red') or (row['R_Stance'] == 'Orthodox' and row['Winner'] == 'Blue'):
#                 orthodox_loss_inst += 1




#     switch_win_inst = 0

#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Switch' and row['Winner'] == 'Blue') or (row['R_Stance'] == 'Switch' and row['Winner'] == 'Red'):
#                 switch_win_inst += 1


#     switch_total = 0

#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Switch') or (row['R_Stance'] == 'Switch'):
#                 switch_total += 1


#     orthodox_total = 0

#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Orthodox') or (row['R_Stance'] == 'Orthodox'):
#                 orthodox_total += 1


#     southpaw_total = 0

#     for index, row in data.iterrows():
#             if (row['B_Stance'] == 'Orthodox') or (row['R_Stance'] == 'Orthodox'):
#                 southpaw_total += 1


#     percentage_switch = switch_win_inst / switch_total 
#     percentage_orthodox = orthodox_win_inst / orthodox_total
#     percentage_southpaw = southpaw_win_inst / southpaw_total

#     percentage_switch_loss = (switch_total - switch_win_inst) / switch_total 
#     percentage_orthodox_loss = (orthodox_total - orthodox_win_inst) / orthodox_total
#     percentage_southpaw_loss = (southpaw_total - southpaw_win_inst) / southpaw_total



#     print(percentage_orthodox)
#     print(percentage_southpaw)
#     print(percentage_switch)

#     print(percentage_orthodox_loss)
#     print(percentage_southpaw_loss)
#     print(percentage_switch_loss)


#     colors = ['aqua', 'red', 'yellow']  
#     label_distance = 1.009
#     labels_stance = ['Orthodox', 'Southpaw', 'Switch']
#     sizes_stance = [percentage_orthodox, percentage_southpaw, percentage_switch]

#     percentage_orthodox_win = percentage_orthodox
#     percentage_southpaw_win = percentage_southpaw
#     percentage_switch_win = percentage_switch

#     percentage_orthodox_loss = percentage_orthodox_loss
#     percentage_southpaw_loss = percentage_southpaw_loss
#     percentage_switch_loss = percentage_switch_loss

#     stances = ['Orthodox', 'Southpaw', 'Switch']

#     win_percentages = [percentage_orthodox_win, percentage_southpaw_win, percentage_switch_win]
#     loss_percentages = [percentage_orthodox_loss, percentage_southpaw_loss, percentage_switch_loss]

#     bar_width = 0.4
#     bar_positions = range(len(stances))


#     mpl.bar(bar_positions, win_percentages, width=bar_width, label='Win Percentage')
#     mpl.bar([pos + bar_width for pos in bar_positions], loss_percentages, width=bar_width, label='Loss Percentage')

#     mpl.xlabel('Stance')
#     mpl.ylabel('Percentage')
#     mpl.title('Win and Loss Percentages by Stance')
#     mpl.xticks([pos + bar_width/2 for pos in bar_positions], stances)
#     mpl.legend()

#     mpl.tight_layout()
#     mpl.show()