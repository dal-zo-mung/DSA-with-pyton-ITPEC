n = 5
# Graph ကို Matrix ပုံစံဖြင့် (Array Index က 1 ကနေ စတာမို့ ရှေ့မှာ 0 တွေ ထည့်ထားပေးရပါတယ်)
graph = [
    [0, 0, 0, 0, 0, 0], # Question ပေးထားချက် အရ index 1 က စမှာမို့ / Index 0 (မသုံးပါ)
    [0, 0, 1, 0, 1, 0], # Node 1: ချိတ်ဆက်ထားသည် (2, 4)
    [0, 1, 0, 1, 0, 1], # Node 2: ချိတ်ဆက်ထားသည် (1, 3, 5)
    [0, 0, 1, 0, 0, 0], # Node 3: ချိတ်ဆက်ထားသည် (2)
    [0, 1, 0, 0, 0, 1], # Node 4: ချိတ်ဆက်ထားသည် (1, 5)
    [0, 0, 1, 0, 1, 0]  # Node 5: ချိတ်ဆက်ထားသည် (2, 4)
]

visited = [False] * (n + 1)
output_order = []

def traverse(k):
    global visited
    visited[k] = True
    output_order.append(k)
    
    # ပုစ္ဆာပါ loop အတိုင်း i=1 မှ n အထိ စစ်ဆေးခြင်း
    for i in range(1, n + 1):
        if graph[k][i] == 1 and visited[i] == False:
            traverse(i)

# Program စတင်ခြင်း
print("Starting traversal from node 1...")
traverse(1)

print(f"Output Order: {output_order}")
