class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

# Global listHead
list_head = None

def add_node(pos, val):
    global list_head
    new_node = ListNode(val)
    
    if pos == 1:
        # အရှေ့ဆုံးမှာ ထည့်ခြင်း
        new_node.next = list_head
        list_head = new_node
    else:
        prev = list_head
        # i ကို 2 မှ pos-1 အထိ loop ပတ်ခြင်း
        for i in range(2, pos):
            if prev.next:
                prev = prev.next
        
        # ကွင်းဆက် ချိတ်ဆက်ခြင်း
        new_node.next = prev.next
        prev.next = new_node # ပုစ္ဆာရှိ ကွက်လပ်ရဲ့ ans (prev.next)

def print_list():
    curr = list_head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements) + " -> None")

# စမ်းသပ်ကြည့်ခြင်း
add_node(1, 'X')
add_node(2, 'Z')
add_node(2, 'Y') # X -> Y -> Z ဖြစ်သွားမယ်

print_list()
