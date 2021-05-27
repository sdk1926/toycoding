# 카페 주문 프로그래밍 

draft_cafe = {'아메리카노': 4100,
            '카페라떼': 4400,
            '얼그레이티': 4500,
            '달고나 라떼': 3800,
            '망고스무디': 4800
            }

def order_coffee():

    global draft_cafe
    print('메뉴판','카페라떼: 4400','얼그레이티: 4500','달고나 라떼: 3800', '망고스무디: 4800', sep='\n')
    coffee = input('주문하실 음료를 입력해주세요.: ')
    price = int(input('주문하신 음료의 가격을 입력해주세요.: '))
    
    try: 
        if draft_cafe[coffee] == price:
            print(f'주문하신 {coffee} 나왔습니당')
        if draft_cafe[coffee] < price:
            print(f'주문하신 {coffee} 나왔구요', 
                f'거스름돈 {price - draft_cafe[coffee]}원 여기 있습니당',
                sep='\n'
                )
        if draft_cafe[coffee] > price:
            print(f'주문하신 {coffee}는 {draft_cafe[coffee]}원 입니다.',
                f'{draft_cafe[coffee] - price}원을 더 주세요.',
                sep='\n' 
                )
    except: print('주문하실 음료를 정확히 입력해주시거나 가격은 꼭 숫자로 입력해주세요.'), order_coffee()


order_coffee()

    
 