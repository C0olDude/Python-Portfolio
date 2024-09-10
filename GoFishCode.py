
while True:
  num_cards_Alice, num_cards_Bob = input().split()
  num_cards_Alice = int(num_cards_Alice)
  num_cards_Bob = int(num_cards_Bob)
  
  if num_cards_Alice >= 1 and num_cards_Alice <= 500:
    if num_cards_Bob >= 1 and num_cards_Bob <= 500:
      break
    else:
      print()
  else:
    print()
Alice_cards = input()
Bob_cards = input()
Alice_cards_list = Alice_cards.split()
Bob_cards_list = Bob_cards.split()
Alice_pairs = 0
Bob_pairs = 0

duplicates = []
for x in Alice_cards_list:
    if Alice_cards_list.count(x) > 1 and x not in duplicates:
        duplicates.append(x)

for x in range(len(duplicates)):
  if Alice_cards_list.count(duplicates[x])% 2 == 0:
    Alice_pairs += Alice_cards_list.count(duplicates[x])/2
  elif Alice_cards_list.count(duplicates[x])% 2 != 0:
    Alice_pairs += (Alice_cards_list.count(duplicates[x])-1) / 2


duplicates = []
for x in Bob_cards_list:
  if Bob_cards_list.count(x) > 1 and x not in duplicates:
      duplicates.append(x)
for x in range(len(duplicates)):
  if Bob_cards_list.count(duplicates[x])% 2 == 0:
    Bob_pairs += Bob_cards_list.count(duplicates[x])/2
  elif Bob_cards_list.count(duplicates[x])% 2 != 0:
    Bob_pairs += (Bob_cards_list.count(duplicates[x])-1) / 2


if Alice_pairs > Bob_pairs:
  print("Alice wins with", int(Alice_pairs), "pairs")
else:
  print("Bob wins with", int(Bob_pairs), "pairs")
