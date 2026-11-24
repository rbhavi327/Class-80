import pandas as pd
scores = [5,8,10,12,15]
players = pd.Series(scores,index = ["Nightwolf","Starblaze","Pixelking","Cyberfox","Ironstorm"])
print(players)

#Part 2 - Pandas data frame
dict = {"Player":["Nightwolf","Starblaze","Pixelking","Cyberfox","Ironstorm"],"Level":[30,35,42,59,71],
        "Score":[5,8,10,12,15],"Wins":[210,180,370,980,257]}

frame = pd.DataFrame(dict)
print(frame)

print("Row 0:")
print(frame.loc[0])
print("Row 2 to 3:")
print(frame.loc[2:3])

#Part 3
csv = pd.read_csv("leaderboard.csv")
print("first five rows of csv:")
print(csv.head())
print("Last 3 rows of csv:")
print(csv.tail(3))
print("Dataset info")
print(csv.info())

#Part 4
print("Rows with missing values removed:")
csv_clean = csv.dropna()
print(csv_clean)
csv_fill = csv.fillna(0)
print("Rows where Nan is replaced")
print(csv_fill)